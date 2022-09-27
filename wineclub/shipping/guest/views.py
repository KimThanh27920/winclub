from rest_framework_simplejwt import authentication
from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response
from .serializers import ShippingUnitSerializer
from shipping.models import ShippingUnit


class ShippingUnitViewSet(viewsets.ViewSet, generics.ListAPIView):
    serializer_class = ShippingUnitSerializer
    queryset = ShippingUnit.objects.filter(is_active=True)