
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

class ListWineAPI(generics.ListAPIView):
    serializer_class = serializers.WineShortSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = [
        'type__type', 
        'style__style',
        'grape__grape',
        'food__food',
        'region__region',
        'country__country'
        ]
    ordering_fields = [
        'average_rating',
        'sale',
        'price'
        ]
    search_fields = [
        'wine',
        'type__type', 
        'style__style',
        'grape__grape',
        'food__food',
        'region__region',
        'country__country'
    ]
    queryset = models.Wine.objects.filter(
        is_active = True, deleted_at = None)
    
    
