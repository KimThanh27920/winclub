# From django
from django.utils import timezone
# From rest_framework
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt import authentication
# From app
from bases.permissions.rolecheck import IsBusinessOrAdmin, IsOwnerByCreatedBy
from wineries.models import Winery
from .serializers import CouponWriteSerializer, CouponReadSerializer, CouponWriteUpdateSerializer, CouponUpdateImageSerializer
from ..models import Coupon



class CreateListCounponView(generics.ListCreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerByCreatedBy, IsBusinessOrAdmin] 
    # pagination_class = None
    
    def get_queryset(self):
        self.queryset = Coupon.objects.filter(deleted_by=None, created_by=self.request.user)        
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
        
        # print(self.request.user.is_staff)
        if(self.request.user.is_staff == False):    
            instance_winery = Winery.objects.get(account=self.request.user)
            # print(instance_winery.is_active)
            if not(instance_winery.is_active):
                serializer.save(is_active=False)


class RetrieveUpdateDestroyCouponView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerByCreatedBy, IsBusinessOrAdmin]
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
        
        if(self.request.method == "PATCH"):
            self.serializer_class = CouponUpdateImageSerializer
               
        return self.serializer_class
        # return super().get_serializer_class()
    
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
        serializer.save(updated_by=self.request.user)
        if(self.request.user.is_staff == False):
            instance_winery = Winery.objects.get(account=self.request.user)
            if not(instance_winery.is_active):
                serializer.save(is_active=False)
            
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_by = self.request.user
        instance.deleted_at = timezone.now()
        instance.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
       