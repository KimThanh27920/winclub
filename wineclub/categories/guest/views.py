# Rest import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#App import
from categories.models import Type, Style, Grape, Region, Food, Country
from .serializers import (TypeReadSerializer,
                            StyleReadSerializer,
                             GrapeReadSerializer,
                              FoodReadSerializer, 
                               RegionReadSerializer, 
                                CountryReadSerializer, )
from bases.guest.views import BaseGuestListViews


#Categories Guest View
class CategoriesAPIView(APIView):

    def get(self, request, *args, **kwargs):
        
        types = Type.objects.all().exclude(deleted_at__isnull=False).filter(is_active=True).order_by('created_at')
        styles = Style.objects.all().exclude(deleted_at__isnull=False).filter(is_active=True).order_by('created_at')
        grapes = Grape.objects.all().exclude(deleted_at__isnull=False).filter(is_active=True).order_by('created_at')
        region = Region.objects.all().exclude(deleted_at__isnull=False).filter(is_active=True).order_by('created_at')
        foods = Food.objects.all().exclude(deleted_at__isnull=False).filter(is_active=True).order_by('created_at')
        country = Country.objects.all().exclude(deleted_at__isnull=False).filter(is_active=True).order_by('created_at')

        types_serializer = TypeReadSerializer(types,many=True)
        styles_serializer = StyleReadSerializer(styles,many=True)
        grapes_serializer = GrapeReadSerializer(grapes,many=True)
        foods_serializer = FoodReadSerializer(foods,many=True)
        region_serializer = RegionReadSerializer(region,many=True)
        countries_serializer = CountryReadSerializer(country,many=True)
        data = {
            "types": types_serializer.data,
            "styles": styles_serializer.data,
            "grapes":grapes_serializer.data,
            "foods": foods_serializer.data,
            "region": region_serializer.data,
            "countries": countries_serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)  



#Type Admin Viewset
class TypeGuestAPIView(BaseGuestListViews):

    serializer_class = TypeReadSerializer
    queryset = Type.objects.select_related('created_by','updated_by')
    search_fields = ['type']
    ordering_fields = ['type']
       

#Style Admin Viewset
class StyleGuestAPIView(BaseGuestListViews):

    serializer_class = StyleReadSerializer
    queryset = Style.objects.select_related('created_by','updated_by')
    search_fields = ['style']
    ordering_fields = ['style']


#Grape Admin Viewset
class GrapeGuestAPIView(BaseGuestListViews):

    serializer_class = GrapeReadSerializer
    queryset = Grape.objects.select_related('created_by','updated_by')
    search_fields = ['grape']
    ordering_fields = ['grape']  


# Food Admin Viewset
class FoodGuestAPIView(BaseGuestListViews):

    serializer_class = FoodReadSerializer
    queryset = Food.objects.select_related('created_by','updated_by')
    search_fields = ['food']
    ordering_fields = ['food']


# Region Admin Viewset
class RegionGuestAPIView(BaseGuestListViews):

    serializer_class = RegionReadSerializer
    queryset = Region.objects.select_related('created_by','updated_by')
    search_fields = ['region']
    ordering_fields = ['region']


# Countries Admin Viewset
class CountryGuestAPIView(BaseGuestListViews):

    serializer_class = CountryReadSerializer
    queryset = Country.objects.select_related('created_by','updated_by')
    search_fields = ['country']
    ordering_fields = ['country']
