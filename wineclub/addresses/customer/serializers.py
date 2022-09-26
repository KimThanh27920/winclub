from dataclasses import field
from rest_framework import serializers
from ..models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = [
            "id",
            "phone",
            "type",
            "full_name",
            "is_default",
            "street",
            "ward",
            "district",
            "city",
            "country"
        ]

    def validate_phone(self, value):
        try:
            int(value)
            return value
        except:
            raise serializers.ValidationError("phone number is not available")

# class DeliverySerializer(serializers.ModelSerializer):
#     address = AddressSerializer(read_only=True)
#     class Meta:
#         model = Delivery
#         fields = [
#             "id",
#             "full_name",
#             "phone",
#             "is_default",
#             "type",
#             "address",
#         ]

# class CreateDeliverySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Delivery
#         fields = [
#             "id",
#             "full_name",
#             "phone",
#             "is_default",
#             "type",
#         ]
