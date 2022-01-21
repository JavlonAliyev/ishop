
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import  Response
from rest_framework.views import APIView
from main.models import Category, Product
from main.serialazers import CategoryListSerializer, CategorySerializer, ProductListSerializer, ProductSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView


class CategoryView(APIView):
    def get(self, request):
        return Response({
        "categories": CategoryListSerializer(Category.objects.all(), many=True).data
    })
    def post(self, request):
        data = CategorySerializer(data=request.data)
        if not data.is_valid():
            return Response({
                "status": "fail",
                "data": data.errors

            })
        data.save()

        return Response({
            "status": "success",
            "data": CategoryListSerializer(data.instance).data
        })
class CategoryEditview(APIView):
    def get(self, request, pk):
        return Response({
            'category': CategoryListSerializer(Category.objects.get(id=pk)).data
        })

    def put(self, request, pk):
        category = Category.objects.get(id=pk)
        data = CategorySerializer(data=request.data, instance=category)
        if not data.is_valid():
            return Response({
                "status": "fail",
                "data": data.errors

            })
        data.save()

        return Response({
            "status": "success",
            "data": CategoryListSerializer(data.instance).data
        })

    def delete(self, request, pk):
        Category.objects.filter(id=pk).delete()

        return Response({
            "status": "success"
        })


class ProductsView(ListAPIView):
       pagination_class = LimitOffsetPagination
       queryset = Product.objects.all().prefetch_related('category')
       serializer_class = ProductListSerializer


class ProductCreatView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductEditView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

