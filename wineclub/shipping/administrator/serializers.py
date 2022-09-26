from rest_framework import serializers
from shipping.models import ShippingUnit


class ShippingUnitSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    class Meta:
        model = ShippingUnit
        fields = [
                "id",
                "name", 
                "fee", 
                "type", 
                "expected_date",
                "is_active",
                'created_by',
                'updated_by',
                ]
        read_only_fields =['created_by','updated_by' ]

class UpdateStatusShippingUnitSerializer(serializers.ModelSerializer):
    updated_by = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = ShippingUnit
        fields = ["is_active",
                'updated_by',
                ]
        read_only_fields =['updated_by' ]
