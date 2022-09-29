from rest_framework import serializers
from ..models import Wine


class WineShortSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()
    class Meta:
        model = Wine
        fields = [
            "id",
            "wine",
            "type",
            "price",
            "sale",
            "in_stock",
            "average_rating",
            "is_active",
            "status",
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