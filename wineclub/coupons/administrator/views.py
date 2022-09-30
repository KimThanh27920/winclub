from rest_framework import generics, permissions, filters
from rest_framework_simplejwt import authentication
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CouponReadSerializer, CouponWriteUpdateSerializer
from ..models import Coupon



class ListCouponView(generics.ListAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = CouponReadSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['created_by__email', 'is_public', 'is_active', 'type']
    ordering_fields = ['time_start', 'time_end', 'created_at']
        
    def get_queryset(self):
        self.queryset = Coupon.objects.filter(deleted_by=None)
        return super().get_queryset()


class UpdateCouponView(generics.UpdateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = CouponWriteUpdateSerializer
    lookup_url_kwarg = "coupon_id"
    
    def get_queryset(self):
        self.queryset = Coupon.objects.filter(deleted_by=None)
        return super().get_queryset()
    
    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user, is_active =False)
        
       