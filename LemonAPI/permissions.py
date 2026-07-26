# permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        user = request.user
        if not user or not user.is_authenticated:
            return False

        return user.groups.filter(name='manager').exists() or user.is_superuser


class IsManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        is_manager = user.groups.filter(name='manager').exists()
        is_admin = user.username == 'admin' or user.is_superuser

        return is_manager or is_admin
