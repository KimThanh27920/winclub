# From django
from django_filters.rest_framework import DjangoFilterBackend
# From rest_framework
from rest_framework import generics, filters
from rest_framework.response import Response
# From app
from .serializers import WineryDetailSerializer, WineryListSerializer, WineryListDistanceSerializer
from ..models import Winery
# From import list
from geopy.distance import geodesic

        

class ListWineryOfPositionView(generics.ListAPIView):
    serializer_class = WineryListDistanceSerializer
        
    def get_queryset(self):        
        self.queryset = Winery.objects.filter(is_active=True)
        return super().get_queryset()
    
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        winery_position = []
        latitude = self.request.GET.get('latitude')
        longtitude = self.request.GET.get('longtitude')
        distance = self.request.GET.get('distance')
        coords_1 = (latitude, longtitude)
        # Calculate distance
        for obj in serializer.data:
            temp = obj['account']['addresses']
            try:
                coords_2 = (temp[0]['latitude'], temp[0]['longtitude'])                
                distance_ = geodesic(coords_1, coords_2).km 
                if(distance_ < float(distance)):
                    obj['distance'] = distance_
                    winery_position.append(obj)
                    
            except:
                pass
        # Sort algorithumm
        lenth = len(winery_position)
        for i in range(0, lenth - 1):
            for j in range(i + 1, lenth):
                if (winery_position[i]['distance'] < winery_position[j]['distance']):
                    tmp = winery_position[i]['distance']
                    winery_position[i]['distance'] = winery_position[j]['distance']
                    winery_position[j]['distance'] = tmp
        
        return Response(winery_position)    
    

class ListWineryView(generics.ListAPIView):
    serializer_class = WineryListSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
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