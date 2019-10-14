from platform import system

from django.shortcuts import render

def index(request):
    return render(request, "home/templates/index.html", {
        "body_message": "BuySell",
    })
# Create your views here.
