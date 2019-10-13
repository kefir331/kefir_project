from django.shortcuts import render

def index(request):
    return render(request, "index.html", {
        "body_message": "BuySell",
    })
# Create your views here.
