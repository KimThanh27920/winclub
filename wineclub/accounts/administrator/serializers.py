#rest framework imports
from rest_framework import serializers

#App import
from accounts.models import Account
from wineries.models import Winery


#Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):


    class Meta:
        model = Account
        fields =[ 
            'id',
            'full_name',
            'email',
            'phone',
            'birthday',
            'gender',
            'image',
            'stripe_account',
            'points',
            'is_active',
            'last_login',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'full_name': {'read_only': True},
            'email': {'read_only': True},
            'phone': {'read_only': True},
            'birthday': {'read_only': True},
            'gender': {'read_only': True},
            'image': {'read_only': True},
            'stripe_account': {'read_only': True},
            'points': {'read_only': True},
            'last_login': {'read_only': True},
        }


#Customer Block/Active Serializer
class BlockCustomerSerializer(serializers.ModelSerializer) :


    class Meta:
        model = Account
        fields =[ 'id','is_active']
        extra_kwargs = {
            'id': {'read_only': True},
            'is_active': {'write_only': True},
        } 


# Business Serializer
class BusinessSerializer(serializers.ModelSerializer):
    account = CustomerSerializer(read_only=True)

    class Meta:
        model = Winery
        fields =[ 
            'id',
            'account',
            'name',
            'rating_average',
            'reviewer',
            'postal_code',
            'website_url',
            'phone_winery',
            'founded_date',
            'image_cover',
            'is_active',
            'created_at',
            'updated_at'
         ]
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
            'rating_average': {'read_only': True},
            'reviewer': {'read_only': True},
            'postal_code': {'read_only': True},
            'website_url': {'read_only': True},
            'founded_date': {'read_only': True},
            'phone_winery': {'read_only': True},
            'image_cover': {'read_only': True},
            'is_active': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


# Business Retrieve Serializer
class BusinessRetrieveSerializer(serializers.ModelSerializer):
    account = CustomerSerializer(read_only=True)

    class Meta:
        model = Winery
        fields =[ 
            'id',
            'account',
            'name',
            'rating_average',
            'reviewer',
            'description',
            'postal_code',
            'website_url',
            'phone_winery',
            'founded_date',
            'image_cover',
            'is_active',
            'created_at',
            'updated_at'
         ]
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
            'rating_average': {'read_only': True},
            'reviewer': {'read_only': True},
            'description': {'read_only': True},
            'postal_code': {'read_only': True},
            'website_url': {'read_only': True},
            'founded_date': {'read_only': True},
            'phone_winery': {'read_only': True},
            'image_cover': {'read_only': True},
            'is_active': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


#Business Block/Active Serializer
class BlockBusinessSerializer(serializers.ModelSerializer) :


    class Meta:
        model = Winery
        fields =[ 'id','is_active']
        extra_kwargs = {
            'id': {'read_only': True},
            'is_active': {'write_only': True},
        } 

