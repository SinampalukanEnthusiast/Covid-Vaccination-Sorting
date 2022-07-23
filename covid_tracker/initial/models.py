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


class NationalIdHolders(models.Model):
    name = models.CharField(max_length=150, null=True,
                            blank=True,)
    district = models.CharField(max_length=150, null=True,
                                blank=True,)
    birthday = models.CharField(max_length=150, null=True,
                                blank=True,)
    gender = models.CharField(max_length=150, null=True,
                              blank=True,)
    civil_status = models.CharField(max_length=150, null=True,
                                    blank=True,)
    is_vaccinated = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "National ID Holder"
        verbose_name_plural = "National ID Holders"

    def __str__(self):
        return self.name
