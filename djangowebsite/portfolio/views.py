from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"data":
               {"name": "Shreyash Singh",
               "img":"img/slider-img.png"}}
    return render(request, "index.html", context)
