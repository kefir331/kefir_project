from django.urls import path
from home.views import HomeViews
from home import models

from . import views

urlpatterns = [
    path("", HomeViews.as_view(), name="home"),
]