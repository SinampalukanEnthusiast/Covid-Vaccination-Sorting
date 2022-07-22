from django.db import models
from django.forms import CharField


class Districts(models.Model):
    name = models.CharField(max_length=50, null=True,
                            blank=True, verbose_name="District Name")
    vaccinated = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"

    def __str__(self):
        return self.name
