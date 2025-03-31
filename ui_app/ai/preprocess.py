from orjson import loads, dumps
from base64 import b64decode
from io import BytesIO
from PIL import Image
import torch
from torch import load
from torch.utils.data import DataLoader
import numpy as np
from torchvision import transforms

from DigitClassifier_API.model import mnistModel
from ui_app.ai.DigitClassifier_API.train import load_model

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Model, optimizer, and loss initialization
classifier = load_model(
        mnistModel, "weight/modelState.pth", device
    )  # Load the saved model

def preprocess(request_bytes):
    img = loads(request_bytes).get("img")
    img = img.split(",")[1]

    # decode the base64
    img_bytes = b64decode(img)

    # convert the bytes to an img
    img = Image.open(BytesIO(img_bytes))

    # convert to 28x28x4
    img = img.resize((28, 28))
    # img = prp(img)
    # img.show()

    return img

def preprocess_image(image_path, device):

    img = Image.open(image_path)
    img_transform = transforms.Compose([
        transforms.Resize((28, 28)),  # Resize to MNIST image size (if needed)
        transforms.Grayscale(),        # Convert to grayscale (if needed)
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,)) # Normalize the image, adjust if necessary
    ])
    img_tensor = img_transform(img).unsqueeze(0).to(device)  # Add batch dimension
    return img_tensor
def predict_digit(img):
    # img is a PIL Image object
     
    # INIT DATALOADER

    # PREDICT
    # model.predict()

    return 69
