from django.urls import path
from profile.views import AboutView, SecurityView, ReferralView, ProfileView

urlpatterns = [
    path("", ProfileView.as_view(), name="profile"),
    path("about/", AboutView.as_view(), name="about"),
    path("security/", SecurityView.as_view(), name="security"),
    path("referral/", ReferralView.as_view(), name="referral"),
]
