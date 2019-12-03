from django.db import models as m


class Security(m.Model):
    guard = m.BooleanField(null=True)
    authenticator = m.BooleanField(null=True)
    sms = m.BooleanField(null=True)





