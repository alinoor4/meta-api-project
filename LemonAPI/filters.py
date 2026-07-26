import django_filters
from .models import MenuItem


class MenuItemFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        field_name='category__title',
        lookup_expr='iexact',
    )

    class Meta:
        model = MenuItem
        fields = ['category']
