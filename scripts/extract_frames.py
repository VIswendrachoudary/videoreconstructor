import cv2
import os

def extract_frames(video_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Extracting {frame_count} frames at {fps} fps...")

    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_dir, f"frame_{i:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        i += 1

    cap.release()
    print(f"Done! Saved {i} frames in '{output_dir}'")

if __name__ == "__main__":
    video_path = r"D:\spatiotemporal-jigsaw\data\jumbled_video.mp4"
    output_dir = r"data\frames_jumbled"
    extract_frames(video_path, output_dir)
