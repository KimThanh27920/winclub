# From rest_framework
from rest_framework import serializers
# From app
from wineries.models import Winery
from wines.models import Wine
from ..models import  Cart, CartDetail



class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = [
            "id",
            "wine",
            "price",
            "sale"
        ]


class WinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery
        fields = [
            "id",
            "name",            
        ]


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

    
class CartDetailOnlyReadSerializer(serializers.ModelSerializer):
    wine = WineSerializer(read_only=True)
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
    winery = WinerySerializer(read_only=True)
    class Meta:
        model = Cart
        fields = [
            "id",
            "winery",
            "cart_detail"
        ]