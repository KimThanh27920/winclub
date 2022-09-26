from rest_framework import serializers
from ..models import Wine


class WineShortSerializer(serializers.ModelSerializer):
    winery = serializers.StringRelatedField()
    class Meta:
        model = Wine
        fields = [
            "id",
            "wine",
            "winery",
            "price",
            "sale",
            "average_rating",
            "thumbnail",
        ]
    

class WineDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = [
            "id",
            "wine",
            
            "region",
            "country",
            "price",
            "sale",
            "alcohol",
            "type",
            "style",
            "grape",
            "food",
            "serving_temperature",
            "in_stock",
            "net",
            "year",
            "bottle_per_case",
            "descriptions",
            "thumbnail",
            "light_bold",
            "smooth_tannic",
            "dry_sweet",
            "soft_acidic",
            "is_active"
        ]

        extra_kwargs = {
            "is_active": {'write_only': True}
        }