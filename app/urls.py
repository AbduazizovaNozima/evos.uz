from django.urls import path
from . import views

urlpatterns = [
    path("category-list/", views.CategoryListAPIView.as_view()),
    path("product-list/", views.ProductListAPIView.as_view()),
    path("category-product-mixed/", views.CategoryProductMixedListAPIView.as_view()),

]