from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt import authentication

from bases.permissions.rolecheck import IsOwnerByCreatedByOrAdmin
from .serializers import CouponWriteSerializer, CouponReadSerializer, CouponWriteUpdateSerializer
from ..models import Coupon

from datetime import datetime



class CreateListCounponView(generics.ListCreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated] 
    # pagination_class = None
    
    def get_queryset(self):
        self.queryset = Coupon.objects.filter(deleted_by = None, created_by = self.request.user)        
        return super().get_queryset()
    
    def get_serializer_class(self):
        if(self.request.method == "GET"):
            self.serializer_class = CouponReadSerializer
        else:
            self.serializer_class = CouponWriteSerializer
        
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        if(self.request.user.is_business):            
            serializer.save(created_by=self.request.user, updated_by=self.request.user, type="business")
        else:
            serializer.save(created_by=self.request.user, updated_by=self.request.user, type="platform")


class RetrieveUpdateDestroyCouponView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerByCreatedByOrAdmin]
    lookup_url_kwarg = "coupon_id"
    
    def get_queryset(self):
        
        if(self.request.method == "PUT"):
            self.queryset = Coupon.objects.filter(deleted_by = None, created_by = self.request.user)
        else:
            self.queryset = Coupon.objects.filter(deleted_by = None)
        return super().get_queryset()
    
    def get_serializer_class(self):
        if(self.request.method == "GET"):
            self.serializer_class = CouponReadSerializer
        else:
            self.serializer_class = CouponWriteUpdateSerializer
        
        return super().get_serializer_class()
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        if (instance.updated_by.is_staff and instance.is_active == False):
            return Response(data={"message":"Coupon was blocked by Admin"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    
    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_by = self.request.user
        instance.deleted_at = datetime.now()
        instance.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
       