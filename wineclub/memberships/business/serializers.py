# From django
from django.contrib.auth import get_user_model
# From rest_framework
from rest_framework import serializers
# From app
from wineries.models import Winery
from ..models import Membership


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