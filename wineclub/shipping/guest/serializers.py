from rest_framework import serializers
from shipping.models import ShippingUnit


class ShippingUnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShippingUnit
        fields = [
                "id",
                "name", 
                "fee", 
                "type", 
                "expected_date",
                ]