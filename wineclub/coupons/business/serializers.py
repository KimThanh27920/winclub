# From django
from django.contrib.auth import get_user_model
# From rest_framework
from rest_framework import serializers
# From app
from ..models import Coupon

User = get_user_model()



class CouponWriteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Coupon
        fields = [
            "id",
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
    def validate(self, attrs):
        print(attrs['time_start'])
        return super().validate(attrs)
        
    def validate_coupon_amount(self, amount): #bd = birthday      
        if (not(0 < amount < 1000)):
            raise serializers.ValidationError("Invalid amount")
        
        return amount
    
class CouponWriteUpdateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Coupon
        fields = [
            "id",
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
    
    def validate_coupon_amount(self, amount): #bd = birthday      
        if (not(0 < amount < 1000)):
            raise serializers.ValidationError("Invalid amount")
        
        return amount
 
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