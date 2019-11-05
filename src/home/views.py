from platform import system
from django.views.generic import TemplateView
from typing import NamedTuple
from home.models import Currency, Country
from django.shortcuts import render


class HomeViews(TemplateView):
    http_method_names = {"get", "post"}

    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["currency"] = Currency.objects.all()
        context["country"] = Country.objects.all()

        return context


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
        "Main": "BuySellBitcoins Main",
    })
