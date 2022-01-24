from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from cart.models import DeliveryAddress
from cart.serialazers import DeliveryAddressListSerializer, DeliveryAddressSerializer


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
