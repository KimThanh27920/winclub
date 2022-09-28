from rest_framework import serializers
from ..models import Coupon
from django.contrib.auth import get_user_model

User = get_user_model()



class CouponWriteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Coupon
        fields = [
            "code",
            "type_reduce",
            "coupon_value",
            "max_value",
            "min_order_value",
            "individual",
            "currency",
            "title",
            "description",
            "coupon_amount",
            "time_start",
            "time_end",
            "is_public",
            "is_active",         
        ]
    
    
class CouponWriteUpdateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Coupon
        fields = [
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
            "is_public",
            "is_active",         
        ]
    
 
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "is_staff"            
        ]
 
    
class CouponReadSerializer(serializers.ModelSerializer):
    created_by = AccountSerializer(read_only=True)
    updated_by = AccountSerializer(read_only=True)
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
            "is_public",
            "is_active",   
            "created_at",
            "created_by",
            "updated_at",           
            "updated_by",       
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
            "is_public",
            "is_active",   
            "created_at",
            "created_by",
            "updated_at",          
            "updated_by", 
        ]