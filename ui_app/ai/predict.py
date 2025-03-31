from pathlib import Path
import torch  # pytorch
from PIL import Image  # image manipulation (Pillow)
from torch import nn, save, load
from torch.optim import Adam
from torchvision import transforms

from DigitClassifier_API.model import mnistModel
from ui_app.ai.DigitClassifier_API.train import load_model

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the model
classifier = load_model(mnistModel, "weight/modelState.pth", device)  
if classifier is None:
    print("Model loading failed. Exiting.")
    exit()

def preprocess_image(image_path, device):
 
    img = Image.open(image_path)
    img_transform = transforms.Compose([
        transforms.Resize((28, 28)),  # Resize to MNIST image size (if needed)
        transforms.Grayscale(),        # Convert to grayscale (if needed)
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,)) # Normalize the image, adjust if necessary
    ])
    img_tensor = img_transform(img).unsqueeze(0).to(device)  
    return img_tensor

def predict_digit(img_tensor):
    output = classifier(img_tensor)
    predicted_label = torch.argmax(output)
    return predicted_label

def main(image_path):

    img_tensor = preprocess_image(image_path, device)
    predicted_label = predict_digit(img_tensor)
    print(f"Predicted digit: {predicted_label}")


