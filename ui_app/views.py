from django.shortcuts import render
from django.http.response import JsonResponse

from .ai.preprocess import preprocess
from .ai.MNIST import predict_digit


def home(request):
    if request.method == "POST":
        img = preprocess(request.body)
        prdct = predict_digit(img)
        
        return JsonResponse({"digit": int(prdct)})

    return render(request, "ui_app/home.html", {})
