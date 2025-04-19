
from rest_framework import generics
from . import models
from . import serializers


class CategoryListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all().order_by("order")
    serializer_class = serializers.CategorySerializer
    pagination_class = None


class ProductListAPIView(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer
    pagination_class = None

    def get_queryset(self):
        category = self.request.query_params.get("category", None)
        queryset = models.Product.objects.all()

        if category and category.isdigit():
            queryset = queryset.filter(category=category)

        return queryset


class CategoryProductMixedListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all().order_by("order")
    serializer_class = serializers.CategoryProductMixedSerializer
    pagination_class = None
