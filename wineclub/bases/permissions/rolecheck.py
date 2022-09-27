from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()

# def check_role_business(self, request):
#     user = User.objects.get(id = request.user.id)
#     return user.is_business


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    # def has_permission(self, request, view):
    #     print(request.user and request.user.is_authenticated())
    #     return request.user and request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        print(obj.user == request.user)
        return obj.user == request.user