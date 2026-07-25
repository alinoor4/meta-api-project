from django.urls import path
from . import views

urlpatterns = [
    path('category', views.CategoriesView.as_view()),
    path('category/<int:pk>', views.SingleCategoryView.as_view()),
    path('menu-item', views.MenuItemsView.as_view()),
    path('menu-item/<int:pk>', views.SingleMenuItemView.as_view()),
]
