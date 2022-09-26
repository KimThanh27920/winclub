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
            "thumbnail",
            "in_stock",
            "is_active",
            "status",
            "updated_at"
        ]