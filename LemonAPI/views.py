from django.shortcuts import render
from .models import *
from . import serializers
from . import filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = []


class SingleCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]

    filter_backends = []


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all().order_by('featured', '-id')
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]

    ordering_fields = ['price', 'category__price']
    search_fields = ['title', 'category__title']
    filterset_class = filters.MenuItemFilter


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = []


class CartView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerialier


class OrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = serializers.OrderSerializer


class UsersByGroupView(generics.ListCreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        group_name = self.kwargs['group_name']
        return User.objects.filter(groups__name=group_name)


class SingleUserByGroupView(generics.DestroyAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        group_name = self.kwargs['group_name']
        return User.objects.filter(groups__name=group_name)
