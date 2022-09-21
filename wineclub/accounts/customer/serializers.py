from pyexpat import model
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "phone",
            "full_name",
            "birtday",
            "gender",
            "points",
            "stripe_account",
        ]
        read_only_fields = [
            "points",
            "stripe_account",
            "email"
        ]
        
        
class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = [
           "old_password",
           "new_password",
           "confirm_password",
        ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "image"
        ]