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
    ordering_fields = ['price',]

    class Meta:
        model = models.MenuItem
        fields = ['id', 'title', 'price',
                  'featured', 'category', 'category_id']
        extra_kwargs = {
            'id': {'read_only': True},
        }
