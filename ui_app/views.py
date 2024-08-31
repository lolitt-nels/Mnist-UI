from django.shortcuts import render



def home(request):
    if request.method == "POST":
        print("yoo")


    return render(request, "ui_app/home.html", {})
