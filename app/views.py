from rest_framework import generics
from . import models
from . import serializers
from django.shortcuts import render, redirect
from .forms import ProductForm
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
import django_filters


def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProductForm()

    return render(request, 'upload.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')

class CategoryListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all().order_by("order")
    serializer_class = serializers.CategorySerializer
    pagination_class = None


class ProductListAPIView(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
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
