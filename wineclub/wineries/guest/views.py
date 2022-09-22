from rest_framework import generics, filters

from .serializers import WineryDetailSerializer, WineryListSerializer
from ..models import Winery

from django_filters.rest_framework import DjangoFilterBackend


class ListWineryView(generics.ListAPIView):
    serializer_class = WineryListSerializer
    queryset = Winery.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'address']
    filterset_fields = ['rating_average']

    
class DetailWineryView(generics.RetrieveAPIView):
    serializer_class = WineryDetailSerializer
    queryset = Winery.objects.all()
    lookup_url_kwarg = "winery_id"