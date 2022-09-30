from rest_framework import serializers

from ..models import Membership
from wineries.models import Winery

from django.contrib.auth import get_user_model

User = get_user_model()


 
class WinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery
        fields = [
            "id",
            "name"
        ]      
 
 
class AccountSerializer(serializers.ModelSerializer):
    # wineries = WinerySerializer()
    class Meta:
        model = User
        fields = [
            # "wineries",
            "email",
            "image",
            "full_name"        
        ]

class MembershipSerializer(serializers.ModelSerializer):
    users = AccountSerializer(many=True)
    class Meta:
        model = Membership
        fields = [
            "users"
        ]
        
        
class MembershipCreateSerializer(serializers.ModelSerializer):
    # users = AccountSerializer(many=True)
    class Meta:
        model = Membership
        fields = [
            "users"
        ]