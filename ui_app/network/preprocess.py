from orjson import loads, dumps
from base64 import b64decode
from io import BytesIO
from PIL import Image

import numpy as np

def preprocess(request_bytes):    
    img = loads(request_bytes).get("img")
    img = img.split(",")[1]

    # decode the base64
    img_bytes = b64decode(img)

    # convert the bytes to an img
    img = Image.open(BytesIO(img_bytes))

    # convert to 28x28x4
    img = img.resize((28, 28))
    # img.show()

    # convert to matrix
    img = np.array(img)

    # the shape is 28 x 28 x 4
    # the 4 represents the rgba vals
    # we need to convert everything to 0's and 1's

    # convert to a binary 28 x 28
    img = np.where((img == [0, 0, 0, 0]).all(axis=2), 0, 1)

    # convert the 28x28 to a 1x28x28
    img = img[np.newaxis, :, :]

    return img
