from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()

# def check_role_business(self, request):
#     user = User.objects.get(id = request.user.id)
#     return user.is_business


class IsOwnerByCreatedByOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    # def has_permission(self, request, view):
    #     print(request.user and request.user.is_authenticated())
    #     return request.user and request.user.is_authenticated()

    # def has_object_permission(self, request, view, obj):
    #     print(obj.user == request.user)
    #     return (obj.user == request.user) or (obj.created_by == request.user)
    
    def has_object_permission(self, request, view, obj):
        print(obj.created_by)
        return obj.created_by == request.user or request.user.is_staff

    
class IsOwnerByAccount(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    # def has_permission(self, request, view):
    #     print(request.user and request.user.is_authenticated())
    #     return request.user and request.user.is_authenticated()
    
    def has_object_permission(self, request, view, obj):
        print(request.user.is_authenticated)
        return obj.account == request.user


# class IsBusinessAndOwnerOrAdmin(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return bool(request.user and (request.user.is_business or request.user.is_staff))
    
#     def has_object_permission(self, request, view, obj):
#         # print(obj.created_by)
#         # return True
#         # return (obj.user == request.user) or (obj.created_by == request.user)
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         print(obj.owner)
#         print(obj.user.is_admin)
#         return obj.owner == request.user or request.user.is_admin
