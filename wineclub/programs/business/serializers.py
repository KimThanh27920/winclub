# From django
from django.contrib.auth import get_user_model
# From rest_framework
from rest_framework import serializers
# From app
from programs.models import RewardProgram
from coupons.models import Coupon
from wineries.models import Winery


User = get_user_model()



class WinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery
        fields = [
            "id",
            "name"
        ]      

 
class AccountSerializer(serializers.ModelSerializer):
    wineries = WinerySerializer(read_only=True)
    class Meta:
        model = User
        fields = [
            "wineries",
            "email",
            "image",        
        ]


class CouponListSerializer(serializers.ModelSerializer):
    created_by = AccountSerializer(read_only=True)
    class Meta: 
        model = Coupon
        fields = [
            "id",
            "code",
            "type",
            "type_reduce",
            "coupon_value",
            "max_value",
            "min_order_value",
            "currency",
            "image",
            "title",
            "time_start",
            "time_end",    
            "created_by", 
        ]
        read_only_fields = [
            "id",
            "code",
            "type",
            "type_reduce",
            "coupon_value",
            "max_value",
            "min_order_value",
            "currency",
            "image",
            "title",
            "time_start",
            "time_end",    
            "created_by", 
        ]


class RewardProgramWriteSerializer(serializers.ModelSerializer):  
    # created_by = AccountSerializer(read_only=True)
    # updated_by = AccountSerializer(read_only=True)  
    # coupons = CouponListSerializer(many=True)
    class Meta:
        model = RewardProgram
        fields =[
            "id",
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
            'created_at',
            "created_by",
            "updated_at",
            "updated_by"
        ]
        
    def validate(self, attrs):
        if not(attrs['total_price_require'] > 0):
            raise serializers.ValidationError("Invalid total_price_require")
        
        if not(attrs['time_start'] < attrs['time_end']):
            raise serializers.ValidationError("Invalid time end before time start")
        
        return super().validate(attrs)    
        
        
class RewardProgramReadSerializer(serializers.ModelSerializer):
    coupons = CouponListSerializer(read_only=True, many=True)
    created_by = AccountSerializer(read_only=True)
    updated_by = AccountSerializer(read_only=True)
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