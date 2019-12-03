from django.views.generic import UpdateView, ListView
from profile.models import About, Security, Referral


class ProfileView(ListView):
    http_method_names = ("get", "post",)
    template_name = "profile/index.html"

    def get_queryset(self):
        if not self.request.GET:
            return []


class AboutView(UpdateView):
    model = About
    template_name = "profile/index.html"


class SecurityView(UpdateView):
    model = Security
    template_name = "profile/index.html"


class ReferralView(UpdateView):
    model = Referral
    template_name = "profile/index.html"
