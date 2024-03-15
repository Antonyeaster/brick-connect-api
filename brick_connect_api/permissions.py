from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsNotificationsrecipient(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.recipient == request.user:
            return True
        raise PermissionDenied(
            "403 Permission has been denied"
        )

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
