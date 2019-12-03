from django import forms

from profile.models import About, Security, Referral


class ProfileForm(forms.Form):
    about = forms.ModelChoiceField(queryset=About.objects.all(), required=False)
    security = forms.ModelChoiceField(queryset=Security.objects.all(), required=True)
    referral = forms.ModelChoiceField(queryset=Referral.objects.all(), required=False)