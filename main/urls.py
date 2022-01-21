from django.urls import path
from .views import CategoryView, CategoryEditview, ProductsView, ProductCreatView, ProductEditView

app_name = 'main'
urlpatterns = [
     path('category/', CategoryView.as_view(), name="category"),
     path('category/<int:pk>/', CategoryEditview.as_view(), name="category-edit"),
     path('products/', ProductsView.as_view(), name="products"),
     path('product/', ProductCreatView.as_view(), name="product"),
     path('product/<int:pk>/', ProductEditView.as_view(), name="product-edit"),

]