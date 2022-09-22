# rest framework import
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters,status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

#App import
from categories.models import Type, Style, Grape, Region, Food, Country
from .serializers import TypeSerializer,TypeReadSerializer, StyleSerializer, StyleReadSerializer
from wines.models import Wine
# Python imports
from datetime import datetime


#Type Admin Viewset
class TypeAdminAPIView(ModelViewSet):

    serializer_class = {
        "list": TypeReadSerializer,
        "retrieve": TypeReadSerializer,
        "create": TypeSerializer,
        "update": TypeSerializer,
        "delete": TypeSerializer
    }
    
    queryset = Type.objects.exclude(deleted_at__isnull=False).select_related('created_by','updated_by').order_by('updated_at')
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['type']
    filterset_fields = ['is_active']

    def get_serializer_class(self):
        return self.serializer_class[self.action]

    def get_queryset(self):
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user,updated_by=self.request.user)

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

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        if Wine.objects.filter(type=instance).exists() :
            data = {
                "message": "Type has subdata, cannot be deleted! "
            }
            return Response(data,status= status.HTTP_400_BAD_REQUEST)

        instance.deleted_by = self.request.user
        instance.deleted_at = datetime.now()
        instance.save()
       

#Style Admin Viewset
class StyleAdminAPIView(ModelViewSet):

    serializer_class = {
        "list": StyleReadSerializer,
        "retrieve": StyleReadSerializer,
        "create": StyleSerializer,
        "update": StyleSerializer,
        "delete": StyleSerializer
    }
    
    queryset = Style.objects.exclude(deleted_at__isnull=False).select_related('created_by','updated_by').order_by('updated_at')
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['style']
    filterset_fields = ['is_active']

    def get_serializer_class(self):
        return self.serializer_class[self.action]

    def get_queryset(self):
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user,updated_by=self.request.user)

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

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        if Wine.objects.filter(style=instance).exists() :
            data = {
                "message": "Type has subdata, cannot be deleted! "
            }
            return Response(data,status= status.HTTP_400_BAD_REQUEST)

        instance.deleted_by = self.request.user
        instance.deleted_at = datetime.now()
        instance.save()
       
