from dataclasses import field
from rest_framework import serializers
from ..models import  Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = [
            "id",
            "street",
            "ward",
            "district",
            "city",
            "country",
        ]


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