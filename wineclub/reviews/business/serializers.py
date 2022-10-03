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
            "created_by",
            "created_at",
            "updated_by",
            "updated_at"
        ]

class RelyReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            "reply"
        ]