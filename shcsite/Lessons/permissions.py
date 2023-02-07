from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


# class NewPermission(permissions.DjangoModelPermissions):
#     authenticated_users_only = False

class NewPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user.is_staff)
        if request.user.is_staff:
            return True
        return False

    def has_object_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
