from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            "id",
            "content",
            "rating",
            "wine",
            "reply",
            "created_at",
            "updated_at"
        ]