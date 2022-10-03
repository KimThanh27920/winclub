from rest_framework import serializers
from shipping.models import ShippingBusinessService, ShippingUnit
from wines.models import Winery


class ReadOnlyShippingUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingUnit
        fields = [
            "id",
            "name",
            "fee",
            "type",
            "expected_date",
            "is_active"
        ]


class ShippingUnitBusinessSerializer(serializers.ModelSerializer):
    shipping_services = ReadOnlyShippingUnitSerializer(many=True, read_only=True)
    class Meta:
        model = ShippingBusinessService
        fields = [
            "winery",
            "shipping_services"
        ]


class AddShippingUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingBusinessService
        fields = [
            "winery",
            "shipping_services"
        ]
        read_only_fields = fields