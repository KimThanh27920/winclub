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
        ]


class ListReviewsSerializer(serializers.ModelSerializer):

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


class UpdateReviewSerializer(serializers.ModelSerializer):

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
        read_only_fields = [
            "rating",
            "wine",
            "reply",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at"
        ]