from ast import Delete
from tabnanny import check
from turtle import update
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework import pagination
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_simplejwt import authentication
from bases.permisions.business import IsBusiness
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
        