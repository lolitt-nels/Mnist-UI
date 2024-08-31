from django.shortcuts import render
from django.http.response import JsonResponse

from .network.preprocess import preprocess




def home(request):
    if request.method == "POST":        
        img = preprocess(request.body)                

        return JsonResponse({"digit": 9})

    return render(request, "ui_app/home.html", {})
