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
                "is_active",
                'created_by',
                "created_at",
                'updated_by',
                "updated_at"
                
                ]
        read_only_fields =['created_by','updated_by' ]

class UpdateStatusShippingUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingUnit
        fields = [
                "id",
                "name",
                "fee",
                "type",
                "expected_date",
                "is_active",
                "created_by",
                "updated_by",
                "created_at",
                "updated_at"
        ]
        read_only_fields = [
                "name",
                "fee",
                "type",
                "expected_date",
                "created_by",
                "updated_by",
        ]
