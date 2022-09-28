
from rest_framework import serializers
from wineries.models import Winery
class WinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery
        fields = "__all__"