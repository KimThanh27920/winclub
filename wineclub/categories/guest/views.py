#App import
from categories.models import Type, Style, Grape, Region, Food, Country
from .serializers import (TypeReadSerializer,
                            StyleReadSerializer,
                             GrapeReadSerializer,
                              FoodReadSerializer, 
                               RegionReadSerializer, 
                                CountryReadSerializer, )
from wines.models import Wine
from bases.guest.views import BaseGuestViewset


#Type Guest View
class TypeAPIView(BaseGuestViewset):

    serializer_class = {
        "list": TypeReadSerializer,
        "retrieve": TypeReadSerializer,
    }
    pagination_class = None
    queryset = Type.objects.all()
       

#Style Guest View
class StyleAPIView(BaseGuestViewset):

    serializer_class = {
        "list": StyleReadSerializer,
        "retrieve": StyleReadSerializer,
    }
    pagination_class = None
    queryset = Style.objects.all()


#Grape Guest View
class GrapeAPIView(BaseGuestViewset):

    serializer_class = {
        "list": GrapeReadSerializer,
        "retrieve": GrapeReadSerializer,
    }
    pagination_class = None
    queryset = Grape.objects.all()


# Food Guest View
class FoodAPIView(BaseGuestViewset):

    serializer_class = {
        "list": FoodReadSerializer,
        "retrieve": FoodReadSerializer,
    }
    pagination_class = None
    queryset = Food.objects.all()


# Region Guest View
class RegionAPIView(BaseGuestViewset):

    serializer_class = {
        "list": RegionReadSerializer,
        "retrieve": RegionReadSerializer,
    }
    pagination_class = None
    queryset = Region.objects.all()


# Countries Guest View
class CountryAPIView(BaseGuestViewset):

    serializer_class = {
        "list": CountryReadSerializer,
        "retrieve": CountryReadSerializer,
    }
    pagination_class = None
    queryset = Country.objects.all()

