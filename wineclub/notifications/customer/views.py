from email import message
from tkinter import N
from rest_framework import status
from rest_framework import filters
from rest_framework import generics, views
from rest_framework import permissions
from rest_framework import pagination
from rest_framework.response import Response
from django.utils import timezone

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_simplejwt import authentication
from . import serializers
from .. import models
from fcm_django.models import FCMDevice
from bases.services.firebase.notification import get_device_user, send_notify_message
class ListCreateDeviceAPI(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.JWTAuthentication]
    serializer_class=serializers.FCMDeviceSerializer
    
    def get_queryset(self):
        return FCMDevice.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

"""
function test send notify to fe
not available public API
"""
class TestSendNotifyAPI(views.APIView):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.JWTAuthentication]

    def post(self, request):
        device = get_device_user(self.request.user.id)
        send_notify_message(device, "hello", "body")
        return Response()
