from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import DeliveryAddress, Order
from cart.serialazers import DeliveryAddressListSerializer, DeliveryAddressSerializer, OrderSerializer, \
    OrderListSerializer


class DeliveryAddressListSerializer(ListAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressListSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)

class DeliveryAddressCreatView(CreateAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()

class DeliveryAddressEditView(RetrieveUpdateDestroyAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer
    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)

class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.validated_data['user'] = self.request.user
            serializer.save()

class OrderListView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all().prefetch_related('delivery_address',
                                                    'delivery_address__country',
                                                    'delivery_address__region',
                                                    'delivery_address__district',
                                                    'orderproduct_set',
                                                    'orderproduct_set__product')
    serializer_class = OrderListSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)


class OrderStatusView(APIView):
    def post(self, request, pk, status):
        if status not in set ([row[0] for row in Order.STATUS_LIST]):
            raise ValidationError({
                "status": "Status qiymati noto'g'ri"
            })

        Order.objects.filter(id=pk).update(status=status)

        return Response({
            "status": status
        })