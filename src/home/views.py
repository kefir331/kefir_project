from collections import defaultdict
from platform import system
from django.views.generic import ListView
from typing import NamedTuple

from home.form import SearchForm
from home.models import UserPosition

from django.shortcuts import render

from home.models import Country


class HomeViews(ListView):
    http_method_names = ("get", "post",)
    template_name = "home/index.html"
    model = UserPosition

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            form = SearchForm(self.request.GET)
            country_id = form.data.get("country")
            country = Country.objects.filter(pk=country_id).first()
        else:
            country = Country.objects.first()
            form = SearchForm(initial={"country": country})

        context["form"] = form
        context["country"] = country

        return context

    def get_queryset(self):
        if not self.request.GET:
            return []

        form = SearchForm(self.request.GET)
        if not form.is_valid():
            return []

        history = super().get_queryset()

        if form.cleaned_data["currency"]:
                history = history.filter(currency=form.cleaned_data["currency"])

        if form.cleaned_data["country"]:
                history = history.filter(country=form.cleaned_data["country"])

        grouped = defaultdict(list)

        for h in history:
            grouped[h.country].append(h)

        return grouped.items()


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
