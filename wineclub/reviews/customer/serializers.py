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
    
    def validate_rating(self, attrs):
        if not(0 < attrs < 6 ):
            raise serializers.ValidationError("rating from 1 to 5")
        return attrs


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