from rest_framework import serializers
from ..models import  Cart, CartDetail



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "winery",
            "account"
        ]
        

class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = [
            "cart",
            "wine",
            "quantity"
        ]