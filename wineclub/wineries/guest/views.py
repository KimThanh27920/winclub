from rest_framework import generics, filters
from rest_framework.views import APIView

from .serializers import WineryDetailSerializer, WineryListSerializer
from ..models import Winery

from django_filters.rest_framework import DjangoFilterBackend

from geopy.distance import geodesic



# class DistanceWinery(APIView):
#     def get(self):
#         Winery.objects.all()
        

class ListWineryOfPositionView(generics.ListAPIView):
    serializer_class = WineryListSerializer
    queryset = Winery.objects.all()
    
    def get_queryset(self):
        coords_1 = (52.2296756, 21.0122287)
        coords_2 = (52.406374, 16.9251681)
        print(geodesic(coords_1, coords_2).km) 
        return super().get_queryset()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ListWineryView(generics.ListAPIView):
    serializer_class = WineryListSerializer
    queryset = Winery.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'address']
    filterset_fields = ['rating_average']
    
    def get_queryset(self):
        coords_1 = (52.2296756, 21.0122287)
        coords_2 = (52.406374, 16.9251681)
        print(geodesic(coords_1, coords_2).km) 
        return super().get_queryset()

class DetailWineryView(generics.RetrieveAPIView):
    serializer_class = WineryDetailSerializer
    queryset = Winery.objects.all()
    lookup_url_kwarg = "winery_id"
    
    
# class ListWineryWithCoordinate(generics.ListAPIView):
#     serializer_class = WineryDetailSerializer