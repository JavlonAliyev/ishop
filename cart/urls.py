from django.urls import path
from .views import DeliveryAddressListSerializer, DeliveryAddressCreatView, DeliveryAddressEditView
from .views import OrderCreateView,OrderListView
app_name = 'cart'

urlpatterns = [
    path('delivery-addresses/', DeliveryAddressListSerializer.as_view(), name="delivery-address-list"),
    path('delivery-address/', DeliveryAddressCreatView.as_view(), name="delivery-address-creat"),
    path('delivery-address/<int:pk>/', DeliveryAddressEditView.as_view(), name="delivery-address-edit"),
    path('orders/',OrderListView.as_view(), name="orders"),
    path('order/', OrderCreateView.as_view(), name="order")


]