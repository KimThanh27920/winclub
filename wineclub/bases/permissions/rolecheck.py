from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()



class IsOwnerByCreatedBy(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        # print(obj.created_by)
        return obj.created_by == request.user

    
class IsOwnerByAccount(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        return obj.account == request.user


class IsBusinessOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (request.user.is_business or request.user.is_staff))

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
