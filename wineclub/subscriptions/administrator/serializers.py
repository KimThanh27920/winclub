#Rest framework imports
from rest_framework import serializers
#Django imports
from django.contrib.auth import get_user_model
#App imports
from subscriptions.models import SubscriptionPackage

User = get_user_model()


#Subscriptions Package Read Serializer
class SubscriptionPackageReadSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = SubscriptionPackage
        fields =[
            'id',
            'name',
            'price',
            'descriptions',
            'currency',
            'interval',
            'interval_count',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by' 
        ]

        read_only_fields =[
            'id',
            'name',
            'price',
            'descriptions',
            'currency',
            'interval',
            'interval_count',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by' 
        ]


#Subscriptions Package Serializer
class SubscriptionPackageSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = SubscriptionPackage
        fields =[
            'id',
            'name',
            'price',
            'descriptions',
            'currency',
            'interval',
            'interval_count',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by' 
        ]

        read_only_fields =[
            'created_at',
            'created_by',
            'updated_at',
            'updated_by' 
        ]

