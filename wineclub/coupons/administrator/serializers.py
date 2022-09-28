from rest_framework import serializers
from ..models import Coupon


# class CouponWriteSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = Coupon
#         fields = [
#             "code",
#             "type_reduce",
#             "coupon_value",
#             "max_value",
#             "min_order_value",
#             "individual",
#             "currency",
#             # "image",
#             "title",
#             "description",
#             "coupon_amount",
#             "time_start",
#             "time_end",
#             "is_public",
#             "is_active",         
#         ]
    
    
class CouponWriteUpdateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Coupon
        fields = [
            "is_active",         
        ]
    
    
class CouponReadSerializer(serializers.ModelSerializer):
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
            "deleted_at",
            "deleted_by",         
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
            "deleted_at",
            "deleted_by",   
        ]