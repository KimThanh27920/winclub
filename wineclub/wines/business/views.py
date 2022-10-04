
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
from wineries.models import Winery
from bases.errors.bases import return_code_400


class ListCreateWineAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.WineShortSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active', 'type__type']
    ordering_fields = ["created_at"]
    search_fields = ["wine"]

    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return serializers.WineWriteSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        return models.Wine.objects.filter(
            deleted_by=None, winery__account=self.request.user)

    def create(self, request, *args, **kwargs):
        self.winery_instance = models.Winery.objects.get(
            account=self.request.user)
        if(not self.winery_instance.is_active):
            self.request.data['is_active'] = False
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = serializers.WineDetailSerializer(self.instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        self.instance = serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user,
            winery=self.winery_instance)


class RetrieveUpdateDestroyWineAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.WineDetailSerializer
    lookup_url_kwarg = "wine_id"

    def get_queryset(self):
        return models.Wine.objects.filter(
            deleted_by=None, winery__account=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        """
        If the request has a wine field, 
        it needs to check wine name exists or not
        """
        try:
            check_wine = models.Wine.objects.get(
                wine=request.data['wine'], created_by=self.request.user)
            if(instance.id != check_wine.id):
                return return_code_400("wine with this wine already exists.")
        except:
            pass

        winery = Winery.objects.get(account=self.request.user)
        """
        if wine is blocked by admin
        or winery not active
        then business does not activate the wine 
        """
        if(instance.is_block or not winery.is_active):
            request.data['is_active'] = False
        serializer = serializers.WineUpdateSerializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        serializer = self.get_serializer(instance)

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
