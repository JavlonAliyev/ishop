from rest_framework import serializers
from .models import DeliveryAddress, Order, OrderProduct

class DeliveryAddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        exclude = ('user',)


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        exclude = ('user',)
