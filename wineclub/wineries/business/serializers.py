from re import I
from rest_framework import serializers

from django.contrib.auth import get_user_model
from ..models import Winery

User = get_user_model()



class AccountSerializer(serializers.ModelSerializer):
    addresses = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = [
            "image",
            "email",
            "addresses"    
        ]
        

class WinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery
        fields = [
            "name",
            "rating_average",
            "reviewer",
            "description",
            "postal_code",
            "website_url",
            "phone_winery",
            "founded_date",
            "image_cover",
        ]
        read_only_fields = [
            "rating_average",
            "reviewer"
        ]
    
    
class WineryProfileSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    class Meta:
        model = Winery
        fields = [
            "account",
            "name",
            "rating_average",
            "reviewer",
            "description",
            "postal_code",
            "website_url",
            "phone_winery",
            "founded_date",
            "image_cover",
        ]
        read_only_fields = [
            "rating_average",
            "reviewer",
        ]
    
    def validate_phone_winery(self, value):
        try:      
            int(value)
            return value
        except:
            raise serializers.ValidationError("Phone number is not available")
        
    def validate_postal_code(self, value):
        print(not(len(value) == 5))
        if not(len(value) == 5):
            raise serializers.ValidationError("PostalCode number don't enough five number") 
        try:             
            int(value)
            return value
        except:
            raise serializers.ValidationError("PostalCode number is not available")

class WineryUploadImageCoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery
        fields = [
            "image_cover"
        ]