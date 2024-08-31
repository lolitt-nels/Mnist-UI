from django.shortcuts import render
from django.http.response import JsonResponse

from orjson import loads, dumps
from base64 import b64decode
from io import BytesIO
from PIL import Image

import numpy as np


def home(request):
    if request.method == "POST":
        img = loads(request.body).get("img")
        img = img.split(",")[1]

        # decode the base64
        img_bytes = b64decode(img)

        # convert the bytes to an img
        img = Image.open(BytesIO(img_bytes))
        # img.show()

        # convert to matrix
        img = np.array(img)
        print(img.shape)

        # the shape is A x A x 4
        # the 4 represents the rgba vals
        # we need to convert everything to 0's and 1's

        # convert to A x A
        img = np.where((img == [0, 0, 0, 0]).all(axis=2), 0, 1)
        #print(img.shape)

        print(img)
        

        return JsonResponse({"digit": 9})

    return render(request, "ui_app/home.html", {})
