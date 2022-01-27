from django.db import models
from account.models import User
from main.models import Product
from common.models import Country, Region, District
from django.utils.translation import gettext_lazy as _

class DeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    county = models.ForeignKey(Country, on_delete=models.RESTRICT)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    district = models.ForeignKey(District, on_delete=models.RESTRICT)
    address = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)

class Order(models.Model):
    STATUS_NEW = 0
    STATUS_ACCEPTED = 1
    STATUS_REJECTED = 2
    STATUS_ON_DELIVERY = 3
    STATUS_DELIVERED = 4
    STATUS_CLOSED = 5

    STATUS_LIST = (
        (STATUS_NEW, _("Yangi")),
        (STATUS_ACCEPTED, _("Qabul qilingan")),
        (STATUS_REJECTED, _("Qaytarilgan")),
        (STATUS_ON_DELIVERY, _("Yo'lda")),
        (STATUS_DELIVERED, _("Yetkazib berilgan")),
        (STATUS_CLOSED, _("Yopilgan"))

    )


    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.RESTRICT)
    total_price = models.BigIntegerField()
    status = models.SmallIntegerField(choices=STATUS_LIST, default=STATUS_NEW)
    order_at = models.DateTimeField(auto_now_add=True)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    price = models.BigIntegerField(default=0)
    quantity = models.IntegerField()

