from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'title',]
        extra_kwargs = {
            'id': {'read_only': True}
        }


class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, min_value=1)

    class Meta:
        model = models.MenuItem
        fields = ['id', 'title', 'price',
                  'featured', 'category', 'category_id']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class CartSerialier(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ['menuitem', 'quantity', 'unit_price', 'price']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['delivery_crew', 'status', 'total', 'date']
