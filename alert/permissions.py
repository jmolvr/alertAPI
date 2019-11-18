from rest_framework import permissions


class isOwner(permissions.BasePermission):
    message = "Not a owner."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.owner
