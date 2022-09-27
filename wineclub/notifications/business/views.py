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
from fcm_django.models import FCMDevice
from .. import models

class ListDeviceAPI(generics.ListAPIView):
    serializer_class = serializers.FCMDeviceSerializer
    queryset = FCMDevice.objects.all()