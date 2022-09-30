from rest_framework import serializers

from addresses.models import Address
from ..models import Winery

from django.contrib.auth import get_user_model

User = get_user_model()



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "is_default",
            "street",
            "ward",
            "district",
            "city",
            "country"
        ]      
       
 
class AccountSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = [
            "image",
            "email",
            "addresses"    
        ]       
       
       
class WineryDetailSerializer(serializers.ModelSerializer):
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
        
        
class WineryListSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    class Meta:
        model = Winery
        fields = [
            "id",
            "account",
            "name",
            "rating_average",
            "reviewer",
            "description",
            "founded_date",
        ]
        read_only_fields = [
            "name",
            "rating_average",
            "reviewer",
            "description",
            "founded_date",
        ]
    
    def to_representation(self, instance):
        limit_content = instance.description
        if len(limit_content) > 100:
            limit_content = limit_content[:100]
            instance.description = limit_content
            instance.description += "..."
    
        return super().to_representation(instance)