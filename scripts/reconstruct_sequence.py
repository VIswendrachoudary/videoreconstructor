import cv2
import os
from tqdm import tqdm

def reverse_video(frames_dir, output_path, fps=30):
  
    frame_files = sorted(
        os.listdir(frames_dir),
        key=lambda x: int(''.join(filter(str.isdigit, x)))
    )

    
    frame_files = frame_files[::-1]

   
    sample_frame = cv2.imread(os.path.join(frames_dir, frame_files[0]))
    h, w, _ = sample_frame.shape

 
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

    
    for fname in tqdm(frame_files, desc="Writing reversed video"):
        frame = cv2.imread(os.path.join(frames_dir, fname))
        if frame is not None:
            out.write(frame)

    out.release()
    print(f"✅ Reversed video saved at: {output_path}")


if __name__ == "__main__":
    frames_dir = r"data/frames_jumbled"
    order_path = r"data/frame_order_final.npy"
    output_path = r"output/reconstructed_video_final_smooth.mp4"

    reverse_video(frames_dir, output_path)
