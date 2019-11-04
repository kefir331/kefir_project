from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('home.urls')),
    path("message/", include('message.urls')),
    path("tradepanel/", include('tradepanel.urls')),
    path("wallet/", include('wallet.urls')),
    path("api/", include('api.urls')),
    path("profile/", include('profile.urls')),
    path("accounts/", include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]