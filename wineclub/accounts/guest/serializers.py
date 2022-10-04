
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from wineries.models import Winery
from memberships.models import Membership
from coupons.models import CouponOwner
from bases.services.stripe.stripe import stripe_created_connect
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

    def validate_phone(self, value):
        try:
            int(value)
            return value
        except:
            raise serializers.ValidationError("phone number is not available")

    def validate_email(self, attrs):
        return attrs.lower()

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        CouponOwner.objects.create(account=user)  # Toan cus
        return user


class AddressSerializer(serializers.Serializer):
    city = serializers.CharField()
    country = serializers.CharField()
    line1 = serializers.CharField()
    line2 = serializers.CharField()
    postal_code = serializers.IntegerField()
    state = serializers.CharField()


class IdentityVerifySerializer(serializers.Serializer):
    first_name = serializers.CharField()
    first_name = serializers.CharField()
    ssn_last_4 = serializers.IntegerField()


class BusinessProfileSerializer(serializers.Serializer):
    url = serializers.URLField()
    mcc = serializers.IntegerField()


class BankAccountSerializer(serializers.Serializer):
    account_holder_name = serializers.CharField()
    routing_number = serializers.IntegerField()
    account_number = serializers.IntegerField()



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

    def validate_phone(self, value):
        try:
            int(value)
            return value
        except:
            raise serializers.ValidationError("phone number is not available")

    def validate_email(self, attrs):
        return attrs.lower()

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class BusinessSerializer(serializers.Serializer):
    address_business = AddressSerializer()
    identity_verify = IdentityVerifySerializer()
    business_profile = BusinessProfileSerializer()
    bank_account = BankAccountSerializer()
    account = BusinessRegisterSerializer()

class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pin
        fields = ['user', 'pin', 'expired']


class ChangePasswordWithPinSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    pin = serializers.IntegerField(required=True)
    new_password = serializers.CharField(required=True)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
