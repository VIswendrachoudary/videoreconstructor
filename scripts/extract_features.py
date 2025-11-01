import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import os
import numpy as np
from tqdm import tqdm

def extract_features(frames_dir, output_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = models.resnet18(pretrained=True)
    model = torch.nn.Sequential(*list(model.children())[:-1])  # remove classifier
    model.to(device)
    model.eval()

    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    frame_files = sorted(os.listdir(frames_dir))
    features = []

    for f in tqdm(frame_files, desc="Extracting features"):
        path = os.path.join(frames_dir, f)
        img = Image.open(path).convert("RGB")
        tensor = preprocess(img).unsqueeze(0).to(device)
        with torch.no_grad():
            feat = model(tensor).cpu().numpy().flatten()
        features.append(feat)

    features = np.array(features)
    np.save(output_path, features)
    print(f"Saved feature vectors to {output_path}")

if __name__ == "__main__":
    print("Feature extraction script started...")
    frames_dir = r"data\frames_jumbled"
    output_path = r"data\frame_features.npy"
    extract_features(frames_dir, output_path)
