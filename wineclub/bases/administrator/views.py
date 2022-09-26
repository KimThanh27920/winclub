# rest framework import
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

# Python imports
# from datetime import datetime
from django.utils import timezone


#Base Admin Viewset
class BaseAdminViewset(ModelViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    def get_serializer_class(self):
        return self.serializer_class[self.action]

    def get_queryset(self):
        return super().get_queryset().exclude(deleted_at__isnull=False).order_by('updated_at')

    def perform_create(self, serializer):
        serializer.save(updated_by=self.request.user,
                        created_by=self.request.user)

    # def list(self, request, *args, **kwargs):
    #     is_paginate = bool(request.query_params.get("paginate",False) == 'true')
    #     if is_paginate:
    #         return super().list(request, *args, **kwargs)
    #     instances = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(instances, many=True)
    #     return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data={"success":True},status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.deleted_by = self.request.user
        instance.is_active = False
        instance.deleted_at = timezone.now()
        instance.save()
