from ast import Delete
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework_simplejwt import authentication
from bases.permisions.business import IsBusiness
from . import serializers
from .. import models

class ListCreateWineAPI(generics.ListCreateAPIView):
    permission_classes = [IsBusiness]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.WineSerializer

    def get_queryset(self):
        return models.Wine.objects.filter(deleted_by = None)