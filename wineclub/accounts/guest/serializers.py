
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from wineries.models import Winery
from .. import models

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate_email(self, attrs):
        return attrs.lower()

    def validate(self, attrs):
        data = super().validate(attrs)
        if(self.user.is_superuser):
            data["permission"] = "admin"
        else:
            if(self.user.is_business):
                data["permission"] = "business"
            else:
                data["permission"] = "customer"
        return data

    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['email'] = user.email
        # ...
        return token

    def to_representation(self, instance):
        return super().to_representation(instance)


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "phone",
            "email",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate_email(self, attrs):
        return attrs.lower()

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)        
        return user

class BusinessRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "phone",
            "email",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate_email(self, attrs):
        return attrs.lower()

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Winery.objects.create(account=user)             #Toan cus
        
        return user

class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pin
        fields = ['user', 'pin']


class ChangePasswordWithPinSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    pin = serializers.IntegerField(required=True)
    new_password = serializers.CharField(required=True)

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)