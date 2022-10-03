from django.contrib.auth import get_user_model

from rest_framework import serializers

from wineries.models import Winery
from ..models import Coupon, CouponOwner

User = get_user_model()


 
class WinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery
        fields = [
            "id",
            "name"
        ]      
 
 
class AccountSerializer(serializers.ModelSerializer):
    wineries = serializers.StringRelatedField()
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
    
    
class CouponDetailSerializer(serializers.ModelSerializer):
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
            "individual",
            "currency",
            "image",
            "title",
            "description",
            "coupon_amount",
            "time_start",
            "time_end",    
            "created_by",  
        ]
        read_only_fields = [
            "code",
            "type",
            "type_reduce",
            "coupon_value",
            "max_value",
            "min_order_value",
            "individual",
            "currency",
            "image",
            "title",
            "description",
            "coupon_amount",
            "time_start",
            "time_end",
        ]


class CouponOwnerReadSerializer(serializers.ModelSerializer):
    coupons = CouponListSerializer(many=True)
    class Meta:
        model = CouponOwner
        fields = [
            "coupons"
        ]