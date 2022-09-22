from re import I
from rest_framework import serializers

from django.contrib.auth import get_user_model
from ..models import Winery

User = get_user_model()



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "image",
            "email"    
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
            "address",
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
            "address",
        ]
        read_only_fields = [
            "rating_average",
            "reviewer",
        ]
    

class WineryUploadImageCoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery
        fields = [
            "image_cover"
        ]