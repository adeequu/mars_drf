from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user #if user is author, the details of post can be viewed only by author


class AnonPermissionOnly(permissions.BasePermission):
    message = "You are already authenticated"

    def has_permission(self, request, view):
        return not request.user.is_authenticated