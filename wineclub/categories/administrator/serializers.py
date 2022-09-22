# rest framework import
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
# App imports
from categories.models import Type, Style, Grape, Region, Food, Country


#Type Read Serializer 
class TypeReadSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    
    class Meta:
        model = Type
        fields =[
            'id',
            'type',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
            
        ] 
        read_only_fields =[
            'type',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by'
        ] 


#Type Serializer 
class TypeSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    
    class Meta:
        model = Type
        fields =[
            'id',
            'type',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',

        ] 
        read_only_fields =['created_by','updated_by' ]
   
    # Allow create a category instance again with name value which was removed
        validators = [
            UniqueTogetherValidator(
                queryset = Type.objects.filter(deleted_by = None),
                fields = ["type"]
            )
        ]


#Style Read Serializer 
class StyleReadSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    
    class Meta:
        model = Style
        fields =[
            'id',
            'style',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
            
        ] 
        read_only_fields =[
            'style',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by'
        ] 


#Style Serializer 
class StyleSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    
    class Meta:
        model = Style
        fields =[
            'id',
            'style',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',

        ] 
        read_only_fields =['created_by','updated_by' ]
   
    # Allow create a category instance again with name value which was removed
        validators = [
            UniqueTogetherValidator(
                queryset = Style.objects.filter(deleted_by = None),
                fields = ["style"]
            )
        ]



#Grape Read Serializer 
class GrapeReadSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    
    class Meta:
        model = Grape
        fields =[
            'id',
            'grape',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
            
        ] 
        read_only_fields =[
            'grape',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by'
        ] 


#Grape Serializer 
class GrapeSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    
    class Meta:
        model = Grape
        fields =[
            'id',
            'grape',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',

        ] 
        read_only_fields =['created_by','updated_by' ]
   
    # Allow create a category instance again with name value which was removed
        validators = [
            UniqueTogetherValidator(
                queryset = Grape.objects.filter(deleted_by = None),
                fields = ["grape"]
            )
        ]


# Food Read Serializer
class FoodReadSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    
    class Meta:
        model = Food
        fields =[
            'id',
            'food',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
            
        ] 
        read_only_fields =[
            'food',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by'
        ] 


# Food Serializer
class FoodSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    
    class Meta:
        model = Food
        fields =[
            'id',
            'food',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',

        ] 
        read_only_fields =['created_by','updated_by' ]
   
    # Allow create a category instance again with name value which was removed
        validators = [
            UniqueTogetherValidator(
                queryset = Food.objects.filter(deleted_by = None),
                fields = ["food"]
            )
        ]


#Region Read Serializer
class RegionReadSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    
    class Meta:
        model = Region
        fields =[
            'id',
            'region',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
            
        ] 
        read_only_fields =[
            'region',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by'
        ] 


#Region Serializer
class RegionSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    
    class Meta:
        model = Region
        fields =[
            'id',
            'region',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',

        ] 
        read_only_fields =['created_by','updated_by' ]
   
    # Allow create a category instance again with name value which was removed
        validators = [
            UniqueTogetherValidator(
                queryset = Region.objects.filter(deleted_by = None),
                fields = ["region"]
            )
        ]


#Country Read Serializer
class CountryReadSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    
    class Meta:
        model = Country
        fields =[
            'id',
            'country',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
            
        ] 
        read_only_fields =[
            'country',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by'
        ] 


#Country Serializer
class CountrySerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    updated_by = serializers.StringRelatedField(read_only = True)
    
    
    class Meta:
        model = Country
        fields =[
            'id',
            'country',
            'is_active',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',

        ] 
        read_only_fields =['created_by','updated_by' ]
   
    # Allow create a category instance again with name value which was removed
        validators = [
            UniqueTogetherValidator(
                queryset = Country.objects.filter(deleted_by = None),
                fields = ["country"]
            )
        ]
