from orjson import loads, dumps
from base64 import b64decode
from io import BytesIO
from PIL import Image

import numpy as np

# IMPORT THE MODEL
# INIT THE MODEL
# model = Model()


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


def predict_digit(img):
    # img is a PIL Image object

    # INIT DATALOADER

    # PREDICT
    # model.predict()

    return 69
