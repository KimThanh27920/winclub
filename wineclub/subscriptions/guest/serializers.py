#rest framework imports
from rest_framework import serializers
#app import
from subscriptions.models import SubscriptionPackage


# Subscription package serializer for guest
class SubscriptionReadOnlySerializer(serializers.ModelSerializer):

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
            
        ]

        read_only_fields =[
            'id',
            'name',
            'price',
            'descriptions',
            'currency',
            'interval',
            'interval_count',
            
        
        ]


#Subscription Package Serializer list for Guest
class SubscriptionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionPackage
        fields =[
            'id',
            'name',
            'price',
            'currency',
            'interval',
            'interval_count',
            
        ]

        read_only_fields =[
            'id',
            'name',
            'price',
            'currency',
            'interval',
            'interval_count',
        
        ]
