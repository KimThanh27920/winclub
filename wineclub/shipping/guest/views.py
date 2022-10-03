from rest_framework import viewsets, generics
from .serializers import ShippingUnitSerializer
from shipping.models import ShippingUnit


class ShippingUnitViewSet(viewsets.ViewSet, generics.ListAPIView):
    serializer_class = ShippingUnitSerializer
    queryset = ShippingUnit.objects.filter(is_active=True)