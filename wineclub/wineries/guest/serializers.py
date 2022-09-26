from re import I
from rest_framework import serializers

from django.contrib.auth import get_user_model
from ..models import Winery

User = get_user_model()


       
class WineryDetailSerializer(serializers.ModelSerializer):
    addresses = serializers.StringRelatedField()
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
            "addresses",
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
            "addresses",
        ]
        
        
class WineryListSerializer(serializers.ModelSerializer):
    addresses = serializers.StringRelatedField()
    class Meta:
        model = Winery
        fields = [
            "id",
            "name",
            "rating_average",
            "reviewer",
            "description",
            "founded_date",
            "addresses",
        ]
        read_only_fields = [
            "name",
            "rating_average",
            "reviewer",
            "description",
            "founded_date",
            "addresses",
        ]
    
    def to_representation(self, instance):
        limit_content = instance.description
        if len(limit_content) > 100:
            limit_content = limit_content[:100]
            instance.description = limit_content
            instance.description += "..."
    
        return super().to_representation(instance)