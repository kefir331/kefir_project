from django.db import models as m


class Referral(m.Model):
    url = m.URLField(unique=True)

