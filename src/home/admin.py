from django.contrib import admin
from . import models

admin.site.register(models.Currency)
admin.site.register(models.Country)