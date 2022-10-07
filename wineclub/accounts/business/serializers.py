
from rest_framework import serializers
from wineries.models import Winery


class WinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery
        fields = "__all__"


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


class ConnectAccountSerializer(serializers.Serializer):
    address_business = AddressSerializer()
    identity_verify = IdentityVerifySerializer()
    business_profile = BusinessProfileSerializer()
    bank_account = BankAccountSerializer()
