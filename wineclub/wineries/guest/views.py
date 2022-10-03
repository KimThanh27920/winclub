# From django
from django_filters.rest_framework import DjangoFilterBackend
# From rest_framework
from rest_framework import generics, filters
from rest_framework.response import Response
# From app
from .serializers import WineryDetailSerializer, WineryListSerializer
from ..models import Winery
# From import list
from geopy.distance import geodesic

        

class ListWineryOfPositionView(generics.ListAPIView):
    serializer_class = WineryListSerializer
    
    def get_queryset(self):
        coords_1 = (52.2296756, 21.0122287)
        coords_2 = (52.406374, 16.9251681)
        print(geodesic(coords_1, coords_2).km) 
        self.queryset = Winery.objects.filter(is_active=False)
        return super().get_queryset()

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)    
    

class ListWineryView(generics.ListAPIView):
    serializer_class = WineryListSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'address']
    filterset_fields = ['rating_average']
    
    def get_queryset(self):
        self.queryset = Winery.objects.filter(is_active=True)
        return super().get_queryset()


class DetailWineryView(generics.RetrieveAPIView):
    serializer_class = WineryDetailSerializer
    lookup_url_kwarg = "winery_id"
    
    def get_queryset(self):
        self.queryset = Winery.objects.filter(is_active=True)
        return super().get_queryset()