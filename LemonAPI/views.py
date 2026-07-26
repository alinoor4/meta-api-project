from django.shortcuts import render
from . import models
from . import serializers
from . import filters
from .permissions import IsManagerOrReadOnly, IsManagerOrAdmin
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class CategoriesView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsManagerOrReadOnly]

    filter_backends = []


class SingleCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsManagerOrAdmin]

    filter_backends = []


class MenuItemsView(generics.ListCreateAPIView):
    queryset = models.MenuItem.objects.all().order_by('featured', '-id')
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [IsManagerOrAdmin]

    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]

    ordering_fields = ['price', 'category__title']
    search_fields = ['title', 'category__title']
    filterset_class = filters.MenuItemFilter


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [IsManagerOrAdmin]

    filter_backends = []
