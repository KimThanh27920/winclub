from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt import authentication

from .serializers import CouponReadSerializer, CouponWriteUpdateSerializer
from ..models import Coupon

from datetime import datetime


class ListCounponView(generics.ListAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = CouponReadSerializer
    
    def get_queryset(self):
        self.queryset = Coupon.objects.filter(deleted_by = None)
        return super().get_queryset()


class UpdateCouponView(generics.UpdateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = CouponWriteUpdateSerializer
    lookup_url_kwarg = "coupon_id"
    
    def get_queryset(self):
        self.queryset = Coupon.objects.filter(deleted_by = None)
        return super().get_queryset()
    
    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user, is_active =False)
        # return super().perform_update(serializer)
        
       