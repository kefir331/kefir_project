from django.db import models

from wallet.models import Withdraw


class Continue(models.Model):
    position = models.DecimalField(max_digits=24, decimal_places=4)

    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "user position"

    def __repr__(self):
        return f"{self.__class__.__name__} #{self.pk}: {self.currency} / {self.country}"

    def __str__(self):
        return f"Price {self.position} {self.currency} of {self.country}"