from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path
from ond.views import SignUpView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path("password-change/done/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
