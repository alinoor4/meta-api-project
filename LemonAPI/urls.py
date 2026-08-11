from django.urls import path
from .views import *

urlpatterns = [
    path('category', CategoriesView.as_view()),
    path('category/<int:pk>', SingleCategoryView.as_view()),
    path('menu-items', MenuItemsView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('groups/<str:group_name>/users', UsersByGroupView.as_view()),
    path('groups/<str:group_name>/users/<int:pk>',
         SingleUserByGroupView.as_view()),
    path('cart/menu-items', CartView.as_view()),
]
