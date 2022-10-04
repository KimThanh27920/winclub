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
    class Meta: 
        model = Coupon
        fields = [
            # "id",
            # "code",
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
        ]
        read_only_fields = [
            # "id",
            # "code",
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
        ]


class CouponDetailSerializer(serializers.ModelSerializer):
    created_by = AccountSerializer(read_only=True)
    class Meta: 
        model = Coupon
        fields = [
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
            "created_by",
        ]
        
        read_only_fields = [
            'id', 
            'name',  
            'total_price_require',
            'coupons',
            'description',
            'time_start',
            'time_end',
            'created_by',
        ]
        
    def to_representation(self, instance):
        limit_content = instance.description
        if len(limit_content) > 100:
            limit_content = limit_content[:100]
            instance.description = limit_content
            instance.description += "..."
    
        return super().to_representation(instance)
    

class RewardProgramReadDetailSerializer(serializers.ModelSerializer):
    coupons = CouponDetailSerializer(read_only=True, many=True)
    created_by = AccountSerializer(read_only=True)
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
            'created_by',
        ]
        
        read_only_fields = [
            'id', 
            'name',  
            'total_price_require',
            'coupons',
            'description',
            'time_start',
            'time_end',
            'created_by',
        ]