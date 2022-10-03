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
        extra_kwargs = {
            "id" : {"read_only" : True},
            "wine" : {"read_only" : True},
            "type" : {"read_only" : True},
            "price" : {"read_only" : True},
            "thumbnail" : {"read_only" : True},
            "in_stock" : {"read_only" : True},
            "updated_at" : {"read_only" : True},
            "created_at" : {"read_only" : True},
            "created_by" : {"read_only" : True},
        }

class AdminBlockWineSerializer(serializers.Serializer):
    is_block = serializers.BooleanField()