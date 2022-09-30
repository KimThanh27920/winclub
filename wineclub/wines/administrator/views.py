
from turtle import update
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework import pagination
from rest_framework.response import Response
from django.utils import timezone

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_simplejwt import authentication
from . import serializers
from .. import models


class ListWineAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.WineShortSerializer
    queryset = models.Wine.objects.filter(deleted_at=None)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ["created_at"]
    search_fields = ["wine", "type__type"]


class UpdateWineAPI(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.WineShortSerializer
    lookup_url_kwarg = "wine_id"
    queryset = models.Wine.objects.filter(deleted_at=None)

    def perform_update(self, serializer):
        serializer.save(
            is_block=self.request.data['is_block'],
            is_active = False,
            updated_by=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
