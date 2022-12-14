from django.db import models

from ishop.decoratrs import i18n

@i18n
class Country(models.Model):
    name_uz = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Davlat"
        verbose_name_plural = "Davlatlar"

    def __str__(self):
      return self.name



@i18n
class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)


@i18n
class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
