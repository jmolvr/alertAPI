from rest_framework import permissions


class isOwner(permissions.BasePermission):
    message = "Not a owner."

    def has_object_permission(self, request, view, obj):
        # print(request.data.get('status'))
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_admin and request.method == 'PUT':
            return True
        return request.user == obj.owner
