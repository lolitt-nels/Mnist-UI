from django.shortcuts import render
from django.http.response import JsonResponse

from .ai.preprocess import preprocess, predict_digit
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    if request.method == "POST":
        img = preprocess(request.body)
        prdct = predict_digit(img)

        return JsonResponse({"digit": prdct})

    return render(request, "ui_app/home.html", {})
