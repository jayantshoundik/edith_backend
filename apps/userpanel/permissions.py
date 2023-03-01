from rest_framework.permissions import BasePermission
from .models import *


class IsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        role = Role.objects.get(role="ADMIN")
        return bool(request.user.is_authenticated and UserRole.objects.filter(user = request.user, role = role).exists())


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_superuser)

