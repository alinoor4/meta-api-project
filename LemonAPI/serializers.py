from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title',]
        extra_kwargs = {
            'id': {'read_only': True}
        }


class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, min_value=1)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price',
                  'featured', 'category', 'category_id']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class CartSerializer(serializers.ModelSerializer):
    menuitem = serializers.SlugRelatedField(
        slug_field='title',
        queryset=MenuItem.objects.all()
    )
    unit_price = serializers.DecimalField(
        max_digits=6, decimal_places=2, read_only=True)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'menuitem', 'quantity', 'unit_price', 'price']
        read_only_fields = ['user', 'unit_price', 'price']

    def create(self, validated_data):
        user = self.context['request'].user
        menuitem = validated_data['menuitem']
        quantity = validated_data['quantity']
        unit_price = menuitem.price

        cart_item, created = Cart.objects.get_or_create(
            user=user,
            menuitem=menuitem,
            defaults={
                'quantity': quantity,
                'unit_price': unit_price,
                'price': unit_price * quantity
            }
        )

        # If already in the cart, increase quantity and total price
        if not created:
            cart_item.quantity += quantity
            cart_item.price = cart_item.quantity * cart_item.unit_price
            cart_item.save()

        return cart_item


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['delivery_crew', 'status', 'total', 'date']


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Group.objects.all(),
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']
        extra_kwargs = {
            'id': {'read_only': True},
        }
