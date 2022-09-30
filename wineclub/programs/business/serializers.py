#rest framework import
from rest_framework import serializers
# App imports
from programs.models import RewardProgram


# Reward Program Serializer
class RewardProgramSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RewardProgram
        fields =[
            'id', 
            'name',  
            'require_sending', 
            'total_price_require',
            'coupons',
            'wines',
            'members',
            'description',
            'start',
            'end',
            'created_at',
        ]
        read_only_fields =['created_at']