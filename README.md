Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML``   # 🎥 Jumbled Video Reconstruction Challenge  This project restores the original order of a **10-second, 1080p (30 FPS)** video whose frames have been randomly shuffled.    It leverages **deep visual similarity (ResNet-18)** and **feature coherence** to rebuild the temporal sequence accurately.  ---  ## 🧩 Objective  Given a shuffled video (`data/jumbled_video.mp4`), the system:  1. Extracts individual frames    2. Generates visual embeddings using a pretrained **ResNet-18** model    3. Infers the correct sequential frame order    4. Rebuilds the video in its original motion flow    ---  ## ⚙️ Requirements  **Python 3.8+**  Install dependencies before running any scripts:  ```bash  pip install opencv-python tqdm numpy torch torchvision pillow   ``

📁 Project Structure
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ├── data/  │   ├── jumbled_video.mp4  │   ├── frames_jumbled/  │   ├── frame_features.npy  │   └── frame_order_final.npy  │  ├── output/  │   └── reconstructed_video_final_smooth.mp4  │  ├── extract_frames.py  ├── extract_features.py  ├── reconstruct_sequence.py  ├── rebuild_video.py  └── README.md   `

💡 **Tip:**If data/ or output/ folders don’t exist, create them manually before running the scripts.

🚀 Usage & Execution Order
--------------------------

### 1️⃣ Extract Frames

Extract all frames from the input video.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python extract_frames.py   `

**Input:** data/jumbled\_video.mp4**Output:** data/frames\_jumbled/frame\_0000.jpg …

### 2️⃣ Extract Frame Features

Generate and save 512-D feature vectors using ResNet-18.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python extract_features.py   `

**Input:** data/frames\_jumbled/**Output:** data/frame\_features.npy

### 3️⃣ Generate Frame Order

Create the correct order file (frame\_order\_final.npy).This step may use custom logic or a separate similarity model.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python reconstruct_sequence.py   `

**Input:** data/frames\_jumbled/**Output:** data/frame\_order\_final.npy

### 4️⃣ Rebuild the Video

Reconstruct the final smooth video in the correct order.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python rebuild_video.py   `

**Inputs:**

*   data/frames\_jumbled/
    
*   data/frame\_order\_final.npy
    

**Output:**output/reconstructed\_video\_final\_smooth.mp4

Execution time is logged automatically in execution\_time.txt.

🧠 Key Design Choices
---------------------

AspectDecisionPurposeFeature EmbeddingResNet-18 (ImageNet pretrained)Captures spatial-semantic frame similarityMatching LogicPairwise feature similarityInfers temporal coherenceOptimizationGPU acceleration, batch processingSpeed & scalabilityModularityIndependent stagesEasy debugging & upgrades

🧮 Complexity (Approx.)
-----------------------

StageTime ComplexityFeature extractionO(N)Similarity computationO(N²)Sorting / reconstructionO(N log N)

For 300 frames, runtime typically stays within a few seconds on a GPU-enabled system.

⚡ Optimization & Parallelism
----------------------------

*   CUDA auto-use when available
    
*   Batch inference for efficient tensor ops
    
*   Vectorized NumPy for similarity computation
    
*   Ready for multiprocessing extensions
    

🧩 Limitations & Future Work
----------------------------

*   Nearly identical frames can confuse ordering
    
*   Optical flow or temporal CNNs could enhance stability
    
*   Graph-based order inference may yield global consistency
    

🎯 Output
---------

✅ **Reconstructed video:** output/reconstructed\_video\_final\_smooth.mp4🕒 **Execution log:** execution\_time.txt📊 **Metrics:** Frame continuity, average similarity (%), runtime efficiency

🏁 Result
---------

The system reconstructs the shuffled video with near-original motion, preserving smooth transitions and temporal integrity.

📘 Algorithm Explanation
------------------------

### 1️⃣ Overview

Reconstruct a shuffled 300-frame video (30 FPS) by inferring temporal relations purely from frame content.

### 2️⃣ Approach

**Step 1 – Frame Extraction**Using OpenCV, every frame is stored sequentially for processing.

**Step 2 – Feature Extraction**Each frame passes through ResNet-18 (pretrained on ImageNet).The classifier head is removed to obtain a 512-D visual embedding per frame.All embeddings are saved in frame\_features.npy.

**Step 3 – Sequence Reconstruction**A predicted order (frame\_order\_final.npy) is generated based on pairwise feature similarity —frames that look alike and follow motion cues are placed adjacently.Local smoothing fixes sharp jumps; reversal detection ensures forward playback.

**Step 4 – Video Rebuilding**Frames are reassembled using OpenCV’s VideoWriter.Frame continuity and order statistics are printed for quick verification.

### 3️⃣ Optimization & Parallelism

*   **GPU Acceleration:** CUDA used automatically when available
    
*   **Batch Processing:** Reduces read/write overhead
    
*   **Vectorized Math:** NumPy replaces explicit Python loops
    
*   **Parallel Extensions:** Ready for multiprocessing on larger datasets
    

### 4️⃣ Design Considerations

AspectDecisionReasonAccuracyDeep visual embeddingsCapture semantics & colorSpeedResNet-18 backboneBalance detail vs. runtimeRobustnessOrder smoothing & reversal checkAvoid local misalignmentsScalabilityModular designEasy extension & parallelization

### 5️⃣ Time Complexity (Approx.)

StageComplexityFeature extractionO(N)Pairwise similarityO(N²)Sorting / reconstructionO(N log N)

For 300 frames, runtime stays within a few seconds on the benchmark system.

### 6️⃣ Limitations & Future Work

*   Nearly identical frames can confuse ordering
    
*   Could be enhanced with optical flow or temporal CNNs
    
*   Future versions may use graph traversal for global order inference
    

### 7️⃣ Result

The reconstructed video closely matches the original temporal flow, maintaining natural motion and minimizing frame discontinuities.
