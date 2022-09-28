from dataclasses import field
from rest_framework import serializers
from fcm_django.models import FCMDevice
from ..models import Notification

class FCMDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FCMDevice
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "title",
            "description",
            "is_check",
            "time"
        ]

        extra_kwargs = {
            "title": {"read_only": True},
            "description": {"read_only": True},
        }