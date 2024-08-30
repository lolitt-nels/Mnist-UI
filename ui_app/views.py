from django.shortcuts import render



def home(request):
    return render(request, "ui_app/home.html", {})
