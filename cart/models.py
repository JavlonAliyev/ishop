from django.db import models
from account.models import User
from main.models import Product
from common.models import Country, Region, District

class DeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    county = models.ForeignKey(Country, on_delete=models.RESTRICT)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    district = models.ForeignKey(District, on_delete=models.RESTRICT)
    address = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.RESTRICT)
    total_price = models.BigIntegerField()
    order_at = models.DateTimeField(auto_now_add=True)

    # @property
    # def products(self):
    #     return OrderProduct.objects.filter(order=self)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    price = models.BigIntegerField(default=0)
    quantity = models.IntegerField()

