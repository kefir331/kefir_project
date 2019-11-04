from django.db import models as m

class Country(m.Model):
    title = m.TextField(unique=True)

    class Meta:
        verbose_name_plural = "country"

    def __repr__(self):
        return f"{self.__class__.__name__} #{self.pk}: {self.title}"

    def __str__(self):
        return f"{self.title} ({self.pk})"
