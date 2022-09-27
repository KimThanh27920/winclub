from rest_framework import serializers
from ..models import  Cart, CartDetail
from wineries.models import Winery


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "account",
            "winery"
        ]
        

class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = [
            "cart",
            "wine",
            "quantity"
        ]
    
    def validate_quantity(self, quantity):
        if not (int(quantity) > 0):
            raise serializers.ValidationError("Invalid quantity")
        
        else:
            return quantity
        
        
class CartDetailUpdateSerializer(serializers.ModelSerializer):      
    class Meta:
        model = CartDetail
        fields = [
            "quantity"
        ]
        
    def validate_quantity(self, quantity):
        if not (quantity > 0):
            raise serializers.ValidationError("Invalid quantity")
        
        else:
            return quantity
    # Serializer for list Cart ==================================================
# class WinerySerializer(serializers.ModelSerializer):

    
class CartDetailOnlyReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = [
            "id",
            "wine",
            "quantity"
        ] 
        read_only_fields = [
            "id",
            "wine",
            "quantity"
        ]
        
class ListCartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailOnlyReadSerializer(many=True)
    class Meta:
        model = Cart
        fields = [
            "id",
            "winery",
            "cart_detail"
        ]