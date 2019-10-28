from django.db import models as m

class Tradeorders(m.Model):
    order_num = m.TextField(unique=True)
    order_url = m.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "tradeorderus"

    def __repr__(self):
        return f"{self.__class__.__name__} #{self.pk}: {self.order_num}"

    def __str__(self):
        return f"{self.order_num} ({self.pk})"