
from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = (
            "id", "name",
        )



class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField()
    #
    # def get_category(self, obj):
    #     return obj.category.name

    class Meta:
        model = models.Product
        fields = (
            "id", "name", 'image', 'description', 'category', 'category_name'
        )


class CategoryProductMixedSerializer(serializers.ModelSerializer):
    # products_list = serializers.SerializerMethodField()
    #
    # def get_products_list(self, obj):
    #     # queryset = models.Product.objects.filter(
    #     #     category=obj
    #     # )
    #     queryset = obj.products.filter()
    #     serializer = ProductSerializer(queryset, many=True)
    #     return serializer.data

    class Meta:
        model = models.Category
        fields = (
            "id", "order", 'name', 'products_list'
        )
