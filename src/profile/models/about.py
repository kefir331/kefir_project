from django.db import models as m


class About(m.Model):
    email = m.EmailField(max_length=128)
    phone = m.DecimalField(max_digits=10, decimal_places=0, unique=True)
    nickname = m.TextField(max_length=10)
    reviews = m.TextField(max_length=256)
    about = m.TextField(max_length=200)
    timezone = m.TextField(unique=True)

