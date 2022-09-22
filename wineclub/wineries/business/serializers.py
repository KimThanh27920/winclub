from rest_framework import serializers

from ..models import Winery


class WinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery
        fields = [
            "name",
            "rating_average",
            "reviewer",
            "description",
            "postal_code",
            "website_url",
            "phone_winery",
            "founded_date",
            "address",
        ]
    read_only_fields = [
        "rating_average",
        "reviewer"
    ]