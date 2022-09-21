<<<<<<< HEAD
from dataclasses import fields
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "email",
            "phone",
            "full_name",
            "birtday",
            "gender",
            "points",
            "stripe_account",
        ]
        read_only_fields = [
            "points"
        ]
        
        
class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
           "password",
           "new_password",
           "confirm_password",
        ]
=======

from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "full_name",
            "phone",
            "email",
            "password"
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate_phone(self, value):
        try:
            int(value)
            if (len(value) != 10):
                raise serializers.ValidationError(
                    "phone number is not available")
            return value
        except:
            raise serializers.ValidationError("phone number is not available")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['email'] = user.email
        # ...
        return token

>>>>>>> 5e904269ef05ed4b928ad685f88064f2ab78ff2c
