from dataclasses import field
from logging import raiseExceptions
from venv import create
from rest_framework import serializers
from ..models import Wine
from categories import models
from rest_framework.validators import ValidationError


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
            "is_block",
            "thumbnail",
        ]


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = [
            "id",
            "region"
        ]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = [
            "id",
            "country"
        ]


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = [
            "id",
            "type"
        ]


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Style
        fields = [
            "id",
            "style"
        ]


class GrapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grape
        fields = [
            "id",
            "grape"
        ]


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = [
            "id",
            "food"
        ]


class WineDetailSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    country = CountrySerializer()
    type = TypeSerializer()
    style = StyleSerializer()
    grape = GrapeSerializer()
    food = FoodSerializer()

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
            "is_active",
            "is_block"
        ]

        extra_kwargs = {
            "is_block": {"read_only": True}
        }


class WineWriteSerializer(serializers.ModelSerializer):
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

    def validate_wine(self, attrs):
        queryset = Wine.objects.filter(
            wine=attrs, created_by=self.context['request'].user)
        if(len(queryset)):
            raise serializers.ValidationError(
                "wine with this wine already exists.")
        else:
            return attrs

    def validate_light_bold(self, attrs):
        if not(0 < attrs < 11):
            raise serializers.ValidationError("value from 1 to 10")
        return attrs

    def validate_smooth_tannic(self, attrs):
        if not(0 < attrs < 11):
            raise serializers.ValidationError("value from 1 to 10")
        return attrs

    def validate_dry_sweet(self, attrs):
        if not(0 < attrs < 11):
            raise serializers.ValidationError("value from 1 to 10")
        return attrs

    def validate_soft_acidic(self, attrs):
        if not(0 < attrs < 11):
            raise serializers.ValidationError("value from 1 to 10")
        return attrs


class WineUpdateSerializer(serializers.ModelSerializer):
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

    def validate_light_bold(self, attrs):
        if not(0 < attrs < 11):
            raise serializers.ValidationError("value from 1 to 10")
        return attrs

    def validate_smooth_tannic(self, attrs):
        if not(0 < attrs < 11):
            raise serializers.ValidationError("value from 1 to 10")
        return attrs

    def validate_dry_sweet(self, attrs):
        if not(0 < attrs < 11):
            raise serializers.ValidationError("value from 1 to 10")
        return attrs

    def validate_soft_acidic(self, attrs):
        if not(0 < attrs < 11):
            raise serializers.ValidationError("value from 1 to 10")
        return attrs
