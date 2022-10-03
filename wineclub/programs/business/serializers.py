# From rest_framework
from rest_framework import serializers
# From app
from programs.models import RewardProgram


# Reward Program Serializer
class RewardProgramWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardProgram
        fields =[
            'name',  
            'total_price_require',
            'coupons',
            'description',
            'time_start',
            'time_end',
            'is_active',
        ]
        
        
class RewardProgramReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardProgram
        fields =[
            'id', 
            'name',  
            'total_price_require',
            'coupons',
            'description',
            'time_start',
            'time_end',
            'is_active',
            'created_at',
            "created_by",
            "updated_at",
            "updated_by"
        ]
        
        read_only_fields = [
            'id', 
            'name',  
            'total_price_require',
            'coupons',
            'description',
            'time_start',
            'time_end',
            'is_active',
            'created_at',
            "created_by",
            "updated_at",
            "updated_by"
        ]