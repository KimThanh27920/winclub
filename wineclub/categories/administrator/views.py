# rest framework import
from rest_framework import status
from rest_framework.response import Response

#App import
from categories.models import Type, Style, Grape, Region, Food, Country
from .serializers import (TypeSerializer,TypeReadSerializer,
                            StyleSerializer, StyleReadSerializer,
                             GrapeReadSerializer, GrapeSerializer,
                              FoodReadSerializer, FoodSerializer,
                               RegionReadSerializer, RegionSerializer,
                                CountryReadSerializer, CountrySerializer)
from wines.models import Wine
from bases.administrator.views import BaseAdminViewset


#Type Admin Viewset
class TypeAdminAPIView(BaseAdminViewset):

    serializer_class = {
        "list": TypeReadSerializer,
        "retrieve": TypeReadSerializer,
        "create": TypeSerializer,
        "update": TypeSerializer,
        "delete": TypeSerializer
    }
    
    queryset = Type.objects.select_related('created_by','updated_by')
    search_fields = ['type']
    filterset_fields = ['is_active']

    def perform_destroy(self, instance):
        if Wine.objects.filter(type=instance).exists() :
            data = {
                "message": "Type has subdata, cannot be deleted! "
            }
            return Response(data,status= status.HTTP_400_BAD_REQUEST)

        return super().perform_destroy(instance)
       

#Style Admin Viewset
class StyleAdminAPIView(BaseAdminViewset):

    serializer_class = {
        "list": StyleReadSerializer,
        "retrieve": StyleReadSerializer,
        "create": StyleSerializer,
        "update": StyleSerializer,
        "delete": StyleSerializer
    }

    queryset = Style.objects.select_related('created_by','updated_by')
    search_fields = ['style']
    filterset_fields = ['is_active']

    def perform_destroy(self, instance):
        if Wine.objects.filter(style=instance).exists() :
            data = {
                "message": "Type has subdata, cannot be deleted! "
            }
            return Response(data,status= status.HTTP_400_BAD_REQUEST)

        return super().perform_destroy(instance)     


#Grape Admin Viewset
class GrapeAdminAPIView(BaseAdminViewset):

    serializer_class = {
        "list": GrapeReadSerializer,
        "retrieve": GrapeReadSerializer,
        "create": GrapeSerializer,
        "update": GrapeSerializer,
        "delete": GrapeSerializer
    }
    
    queryset = Grape.objects.select_related('created_by','updated_by')

    search_fields = ['grape']
    filterset_fields = ['is_active']

    def perform_destroy(self, instance):
        if Wine.objects.filter(grape=instance).exists() :
            data = {
                "message": "Type has subdata, cannot be deleted! "
            }
            return Response(data,status= status.HTTP_400_BAD_REQUEST)

        return super().perform_destroy(instance)     


# Food Admin Viewset
class FoodAdminAPIView(BaseAdminViewset):

    serializer_class = {
        "list": FoodReadSerializer,
        "retrieve": FoodReadSerializer,
        "create": FoodSerializer,
        "update": FoodSerializer,
        "delete": FoodSerializer
    }
    
    queryset = Food.objects.select_related('created_by','updated_by')
    search_fields = ['food']
    filterset_fields = ['is_active']

    def perform_destroy(self, instance):
        if Wine.objects.filter(food=instance).exists() :
            data = {
                "message": "Type has subdata, cannot be deleted! "
            }
            return Response(data,status= status.HTTP_400_BAD_REQUEST)

        return super().perform_destroy(instance)  


# Region Admin Viewset
class RegionAdminAPIView(BaseAdminViewset):

    serializer_class = {
        "list": RegionReadSerializer,
        "retrieve": RegionReadSerializer,
        "create": RegionSerializer,
        "update": RegionSerializer,
        "delete": RegionSerializer
    }
    
    queryset = Region.objects.select_related('created_by','updated_by')
    search_fields = ['region']
    filterset_fields = ['is_active']

    def perform_destroy(self, instance):
        if Wine.objects.filter(region=instance).exists() :
            data = {
                "message": "Type has subdata, cannot be deleted! "
            }
            return Response(data,status= status.HTTP_400_BAD_REQUEST)

        return super().perform_destroy(instance)  


# Countries Admin Viewset
class CountryAdminAPIView(BaseAdminViewset):

    serializer_class = {
        "list": CountryReadSerializer,
        "retrieve": CountryReadSerializer,
        "create": CountrySerializer,
        "update": CountrySerializer,
        "delete": CountrySerializer
    }
    
    queryset = Country.objects.select_related('created_by','updated_by')
    search_fields = ['country']
    filterset_fields = ['is_active']

    def perform_destroy(self, instance):
        if Wine.objects.filter(country=instance).exists() :
            data = {
                "message": "Type has subdata, cannot be deleted! "
            }
            return Response(data,status= status.HTTP_400_BAD_REQUEST)

        return super().perform_destroy(instance)  
