# rest framework import
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

#Base Admin Viewset
class BaseGuestViewset(ModelViewSet):

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    def get_serializer_class(self):
        return self.serializer_class[self.action]

    def get_queryset(self):
        return super().get_queryset().exclude(deleted_at__isnull=False).filter(is_active=True).order_by('created_at')

    def perform_create(self, serializer):
       pass

    def list(self, request, *args, **kwargs):
        is_paginate = bool(request.query_params.get("paginate",False) == 'true')
        if is_paginate:
            return super().list(request, *args, **kwargs)
        instances = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(instances, many=True)
        return Response(serializer.data)

    def perform_update(self, serializer):
        pass

    def perform_destroy(self, instance):
        pass
  
