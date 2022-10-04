# From rest_framework
from rest_framework import serializers
# From app
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

