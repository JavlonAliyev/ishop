from django.db import models

from ishop.decoratrs import i18n
from ishop.helpers import UploadTo


@i18n
class Category(models.Model):
    name_uz = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    image = models.ImageField(upload_to=UploadTo("category"), null=True, blank=True, default=None)

@i18n
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    image = models.ImageField(upload_to=UploadTo("category"), null=True, blank=True, default=None)
    price = models.BigIntegerField()
    available = models.IntegerField(default=None)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

