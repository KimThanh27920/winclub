#rest framework imports
from rest_framework import serializers
#App imports
from categories.models import Type, Style, Grape, Food, Region, Country


#Type Read Serializer 
class TypeReadSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Type
        fields =[
            'id',
            'type',
            
        ] 
        read_only_fields =[
            'id',
            'type',
        ] 


#Style Read Serializer 
class StyleReadSerializer(serializers.ModelSerializer):
      
    
    class Meta:
        model = Style
        fields =[
            'id',
            'style',
        ] 
        read_only_fields =[
            'id',
            'style',
        ] 


#Grape Read Serializer 
class GrapeReadSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Grape
        fields =[
            'id',
            'grape',
        ] 
        read_only_fields =[
            'id',
            'grape',
        ] 


# Food Read Serializer
class FoodReadSerializer(serializers.ModelSerializer):
  
    
    class Meta:
        model = Food
        fields =[
            'id',
            'food',     
        ] 
        read_only_fields =[
            'id',
            'food',
        ] 


#Region Read Serializer
class RegionReadSerializer(serializers.ModelSerializer):
   
    
    class Meta:
        model = Region
        fields =[
            'id',
            'region',
            
        ] 
        read_only_fields =[
            'id',
            'region',
        ] 


#Country Read Serializer
class CountryReadSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Country
        fields =[
            'id',
            'country', 
            
        ] 
        read_only_fields =[
            'id',
            'country',
            
        ] 

   

