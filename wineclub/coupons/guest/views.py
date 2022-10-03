from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Coupon
from .serializers import CouponDetailSerializer, CouponListSerializer



class ListCouponView(generics.ListAPIView):
    serializer_class = CouponListSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['created_by__email', 'type', 'created_by__email']
    ordering_fields = ['time_start', 'time_end', 'created_at']
    
    def get_queryset(self):
        self.queryset = Coupon.objects.filter(is_public=True, is_active=True)
        return super().get_queryset()
    
    
class RetrieveCouponView(generics.RetrieveAPIView):
    serializer_class = CouponDetailSerializer    
    lookup_url_kwarg = 'coupon_id'
    
    def get_queryset(self):
        self.queryset = Coupon.objects.filter(is_public=True, is_active=True)
        return super().get_queryset()