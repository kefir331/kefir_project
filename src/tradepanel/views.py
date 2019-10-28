from django.shortcuts import render

from tradepanel.models import Tradeorders

def tradepanel(request):
    return render(request, "tradepanel/index.html", context={
        "tradeorderus": Tradeorders.objects.all(),
    })
