from rest_framework import serializers
from ..models import Wine


class WineShortSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
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
            "is_block",
            "updated_at",
            "created_at",
            "updated_by",
            "created_by",

        ]