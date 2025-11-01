import cv2
import numpy as np
import os
import time
from tqdm import tqdm
start = time.time()
def rebuild_video(frames_dir, order_path, output_path, fps=30):
    
    order = np.load(order_path)
    frame_files = sorted(
        os.listdir(frames_dir),
        key=lambda x: int(''.join(filter(str.isdigit, x)))
    )

    
    if len(order) != len(frame_files):
        print(f"[WARN] Adjusting order: {len(order)} -> {len(frame_files)}")
        order = order[:len(frame_files)]

   
    order = np.array(order, dtype=int)

    
    diffs = np.diff(order)
    median_jump = np.median(np.abs(diffs))
    for i in range(1, len(order) - 1):
        if abs(order[i] - order[i - 1]) > 3 * median_jump:
            order[i] = (order[i - 1] + order[i + 1]) // 2

    
    forward_score = np.mean(np.diff(order) > 0)
    if forward_score < 0.5:
        order = order[::-1]
        print("↩ Auto-corrected: video was reversed")

   
    print(f"\n Total frames: {len(order)}")
    print(f"Forward continuity score: {forward_score:.4f}")
    print(f"Order sample: {order[:10]} ... {order[-10:]}")

    
    sample_frame = cv2.imread(os.path.join(frames_dir, frame_files[0]))
    h, w, _ = sample_frame.shape
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

    
    for idx in tqdm(order, desc="Writing frames"):
        if 0 <= idx < len(frame_files):
            frame_path = os.path.join(frames_dir, frame_files[idx])
            frame = cv2.imread(frame_path)
            if frame is not None:
                out.write(frame)

    out.release()
    print(f" Reconstructed video saved at: {output_path}")


if __name__ == "__main__":
    
    frames_dir = r"data/frames_jumbled"
    order_path = r"data/frame_order_final.npy"
    output_path = r"output/reconstructed_video_final_smooth.mp4"
    rebuild_video(frames_dir, order_path, output_path)

    
end = time.time()
with open("execution_time.txt", "w") as f:
    f.write(f"Total reconstruction time: {end - start:.2f} seconds\n")
