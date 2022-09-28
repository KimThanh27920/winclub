from rest_framework import serializers
from shipping.models import ShippingBusinessService, ShippingUnit
from wines.models import Winery


class ShippingUnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShippingBusinessService
        fields = [
                "winery",
                "shipping_services",
                "created_at",
                "updated_at"
                ]


class ShippingUnitReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingUnit
        fields = ["id"]




class ShippingUnitDetailSerializer(serializers.ModelSerializer):
    shipping_services = serializers.StringRelatedField(read_only = True, many=True)
    class Meta:
        model = ShippingBusinessService
        fields = [
            "winery",
            "shipping_services",
            "created_at",
            "updated_at"
        ]
        read_only_fields =['winery']


class UpdateShippingUnitBusinessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShippingBusinessService
        fields = [
            "shipping_services",
            "update_at"
        ]