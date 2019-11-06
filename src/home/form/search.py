from django import forms

from home.models import Currency, Country


class SearchForm(forms.Form):
    currency = forms.ModelChoiceField(queryset=Currency.objects.all(), required=False)
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=True)

