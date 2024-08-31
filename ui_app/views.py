from django.shortcuts import render
from django.http.response import JsonResponse


def home(request):
    if request.method == "POST":

        return JsonResponse({})

    return render(request, "ui_app/home.html", {})
