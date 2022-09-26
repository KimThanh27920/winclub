
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
from bases.permisions.business import IsBusiness
from . import serializers
from .. import models


class ListWineAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.WineShortSerializer
    queryset = models.Wine.objects.filter(deleted_at = None)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ["created_at"]
    search_fields = ["wine", "type__type"]

class UpdateWineAPI(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.WineShortSerializer
    lookup_url_kwarg = "wine_id"
    queryset = models.Wine.objects.filter(deleted_at = None)
    
    def perform_update(self, serializer):
        serializer.save(status = self.request.data['status'], updated_by = self.request.user)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)