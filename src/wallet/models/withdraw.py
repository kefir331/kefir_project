from django.db import models as m


class Withdraw(m.Model):
    receiving = m.TextField(unique=True)
    amount = m.TextField(null=True, blank=True)
    description = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "tradeorderus"

    def __repr__(self):
        return f"{self.__class__.__name__} #{self.pk}: {self.receiving}"

    def __str__(self):
        return f"{self.receiving} ({self.pk})"
