from platform import system
from typing import NamedTuple

from django.core.signing import Signer
from django.shortcuts import render


class TabContent(NamedTuple):
    content: str


def buyers():
    return {
        "Buyer": TabContent("Nickname"),
        "Payment method": TabContent("National Bank"),
        "Price": TabContent("20000"),
        "Limit": TabContent("1-10000"),
    }


def sellers():
    return {
        "Seller": TabContent("Nickname"),
        "Payment method": TabContent("National bank"),
        "Price": TabContent("18500"),
        "Limit": TabContent("1-15000"),
    }


def actual(request):
    return render(request, "home/index.html", {
        "buyobject": buyers().items(),
        "sellobject": sellers().items(),
        "body_message": "BuySell",
        "Main": "BuySellBitcoins Main",
    })
# Create your views here.
