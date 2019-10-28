from django.urls import path
from tradepanel import views

urlpatterns = [
    path("", views.tradepanel, name="tradepanel")]