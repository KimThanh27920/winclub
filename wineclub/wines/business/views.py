
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework import pagination
from rest_framework.response import Response
from django.utils import timezone

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_simplejwt import authentication
from bases.permissions.business import IsBusiness
from . import serializers
from .. import models


class ListCreateWineAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.WineShortSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ["created_at"]
    search_fields = ["wine", "type__type"]

    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return serializers.WineDetailSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        return models.Wine.objects.filter(
            deleted_by=None, winery__account=self.request.user)

    def perform_create(self, serializer):
        winery_instance = models.Winery.objects.get(account = self.request.user)
        serializer.save(
            created_by = self.request.user,
            updated_by = self.request.user,
            winery = winery_instance)

class RetrieveUpdateDestroyWineAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.WineDetailSerializer
    lookup_url_kwarg = "wine_id"
    
    def get_queryset(self):
        return models.Wine.objects.filter(
            deleted_by=None, winery__account=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def perform_destroy(self, instance):
        instance.deleted_by = self.request.user
        instance.wine = str(instance.wine) + str(timezone.now())
        instance.is_active = False
        instance.deleted_at = timezone.now()
        instance.save()

    