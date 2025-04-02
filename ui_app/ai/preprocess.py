from pathlib import Path
from orjson import loads, dumps
from base64 import b64decode
from io import BytesIO
from PIL import Image
import torch
from torch import load
from torch.utils.data import DataLoader
import numpy as np
from torchvision import transforms

from ui_app.ai.MNIST.model import mnistModel

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
def load_model(model_class, model_path, device):

    classifier = model_class().to(device)
    if Path(model_path).exists():
        try:
            classifier.load_state_dict(torch.load(model_path, map_location=device))
            print(f"Successfully loaded model from {model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
    else:
        print("No saved model found. Starting from scratch.")
    return classifier




# Load the model
classifier = load_model(mnistModel, "ui_app/ai/MNIST/weight/modelState.pth", device)  
if classifier is None:
    print("Model loading failed. Exiting.")
    exit()



def preprocess(request_bytes):
    # Load the image from the API request
    img_data = loads(request_bytes).get("img")
    img_data = img_data.split(",")[1]

    # Decode the base64 string
    img_bytes = b64decode(img_data)

    # Convert the bytes to a PIL Image
    img = Image.open(BytesIO(img_bytes))

    # Apply transformations
    img_transform = transforms.Compose([
        transforms.Grayscale(),        # Convert to grayscale
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,)) # Normalize the image
    ])
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Apply transformations and resize to 28x28
    img = img.resize((28, 28))  # Resize to MNIST size
    img_tensor = img_transform(img).unsqueeze(0).to(device)

    return img_tensor


def predict_digit(img_tensor):
    output = classifier(img_tensor)
    predicted_label = torch.argmax(output).item() 
   
    return predicted_label
