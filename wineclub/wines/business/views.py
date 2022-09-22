from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework_simplejwt import authentication

from . import serializers
from .. import models

class ListCreateCustomerAddressAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.DeliverySerializer

    def get_queryset(self):
        return models.Wine.objects.filter()