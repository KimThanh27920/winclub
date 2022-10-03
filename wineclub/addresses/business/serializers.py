from dataclasses import field
from rest_framework import serializers
from ..models import Address


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
            "latitude",
            "longtitude"
        ]

