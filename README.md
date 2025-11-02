🎥 **Jumbled Video Reconstruction Challenge**

This project restores the original order of a 10-second, 1080p (30 FPS) video whose frames have been randomly shuffled.
It leverages deep visual similarity (ResNet-18) and feature coherence to rebuild the temporal sequence accurately.

---

## 🧩 Objective

Given a shuffled video (`data/jumbled_video.mp4`), the system:

1. Extracts individual frames
2. Generates visual embeddings using a pretrained ResNet-18 model
3. Infers the correct sequential frame order
4. Rebuilds the video in its original motion flow

---

## ⚙️ Requirements

**Python 3.8+**

Install dependencies before running any scripts:

pip install opencv-python tqdm numpy torch torchvision pillow

---

## 📁 Project Structure

data/
│── jumbled_video.mp4
│── frames_jumbled/
│── frame_features.npy
│── frame_order_final.npy

output/
│── reconstructed_video_final_smooth.mp4

extract_frames.py
extract_features.py
reconstruct_sequence.py
rebuild_video.py
README.md

💡 Tip:
If `data/` or `output/` folders don’t exist, create them manually before running the scripts.

---

## 🚀 Usage & Execution Order

1️⃣ **Extract Frames**

Extract all frames from the input video.

python extract_frames.py
Input: data/jumbled_video.mp4
Output: data/frames_jumbled/frame_0000.jpg …

---

2️⃣ **Extract Frame Features**

Generate and save 512-D feature vectors using ResNet-18.

python extract_features.py
Input: data/frames_jumbled/
Output: data/frame_features.npy

---

3️⃣ **Generate Frame Order**

Create the correct order file (frame_order_final.npy).
This step may use custom logic or a separate similarity model.

python reconstruct_sequence.py
Input: data/frames_jumbled/
Output: data/frame_order_final.npy

---

4️⃣ **Rebuild the Video**

Reconstruct the final smooth video in the correct order.

python rebuild_video.py
Inputs:
• data/frames_jumbled/
• data/frame_order_final.npy

Output: output/reconstructed_video_final_smooth.mp4

Execution time is logged automatically in execution_time.txt.

---

## 🧠 Key Design Choices

Feature Embedding: ResNet-18 (ImageNet pretrained) → Captures spatial-semantic frame similarity
Matching Logic: Pairwise feature similarity → Infers temporal coherence
Optimization: GPU acceleration, batch processing → Speed & scalability
Modularity: Independent stages → Easy debugging & upgrades

---

## 🧮 Complexity (Approx.)

Feature extraction – O(N)
Similarity computation – O(N²)
Sorting / reconstruction – O(N log N)

For 300 frames, runtime typically stays within a few seconds on a GPU-enabled system.

---

## ⚡ Optimization & Parallelism

• CUDA auto-use when available
• Batch inference for efficient tensor ops
• Vectorized NumPy for similarity computation
• Ready for multiprocessing extensions

---

## 🧩 Limitations & Future Work

• Nearly identical frames can confuse ordering
• Optical flow or temporal CNNs could enhance stability
• Graph-based order inference may yield global consistency

---

## 🎯 Output

✅ Reconstructed video: output/reconstructed_video_final_smooth.mp4
🕒 Execution log: execution_time.txt
📊 Metrics: Frame continuity, average similarity (%), runtime efficiency

---

## 🏁 Result

The system reconstructs the shuffled video with near-original motion, preserving smooth transitions and temporal integrity.

---

## 📘 Algorithm Explanation

**Step 1 – Frame Extraction**
Using OpenCV, every frame is stored sequentially for processing.

**Step 2 – Feature Extraction**
Each frame passes through ResNet-18 (pretrained on ImageNet).
The classifier head is removed to obtain a 512-D visual embedding per frame.
All embeddings are saved in frame_features.npy.

**Step 3 – Sequence Reconstruction**
A predicted order (frame_order_final.npy) is generated based on pairwise feature similarity —
frames that look alike and follow motion cues are placed adjacently.
Local smoothing fixes sharp jumps; reversal detection ensures forward playback.

**Step 4 – Video Rebuilding**
Frames are reassembled using OpenCV’s VideoWriter.
Frame continuity and order statistics are printed for quick verification.

---

## ⚙️ Optimization Details

GPU Acceleration – CUDA used automatically when available
Batch Processing – Reduces read/write overhead
Vectorized Math – NumPy replaces explicit Python loops
Parallel Extensions – Ready for multiprocessing on larger datasets

---

## 💡 Design Considerations

Accuracy – Deep visual embeddings capture semantics and color
Speed – ResNet-18 balances detail vs. runtime
Robustness – Order smoothing & reversal check avoid local misalignments
Scalability – Modular design supports easy extension

---

## ⏱️ Time Complexity (Approx.)

Feature extraction – O(N)
Pairwise similarity – O(N²)
Sorting / reconstruction – O(N log N)

For 300 frames, runtime stays within a few seconds on the benchmark system.

---

## 🚧 Limitations & Future Work

• Nearly identical frames can confuse ordering
• Could be enhanced with optical flow or temporal CNNs
• Future versions may use graph traversal for global order inference

---

## ✅ Result

The reconstructed video closely matches the original temporal flow, maintaining natural motion and minimizing frame discontinuities.

---

End of Document ✅
