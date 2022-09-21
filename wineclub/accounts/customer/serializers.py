from dataclasses import fields
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
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
            "points"
        ]
        
        
class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
           "password",
           "new_password",
           "confirm_password",
        ]
