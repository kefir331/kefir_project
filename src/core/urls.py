from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('home.urls')),
    path("about/", include('about.urls')),
    path("graphics/", include('graphics.urls')),
    path("dynamics/", include('dynamics.urls')),
    path('admin/', admin.site.urls),
]
