# From django
from django.utils import timezone
# From rest_framework
from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework_simplejwt import authentication
from django_filters.rest_framework import DjangoFilterBackend
# From app
from bases.permissions.business import IsBusiness
from bases.errors.bases import return_code_400
from coupons.models import Coupon
from wineries.models import Winery
from .serializers import RewardProgramWriteSerializer, RewardProgramReadSerializer
from ..models import RewardProgram



class ProgramListCreateView(generics.ListCreateAPIView):
    serializer_class = RewardProgramReadSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at']
    filterset_fields = ['is_active']
    
    def get_queryset(self):
        self.queryset = RewardProgram.objects.filter(created_by=self.request.user.id, deleted_by=None)
        return self.queryset
    
    def get_serializer_class(self):
        if(self.request.method == "POST"):
            self.serializer_class = RewardProgramWriteSerializer
            return self.serializer_class
        
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        for coupon in serializer.validated_data['coupons']:
            instance_coupon = Coupon.objects.filter(code=coupon, created_by=self.request.user, is_active=True, is_public=False) 
            if not(instance_coupon.exists()):
                message = "You don't own this coupon Or Coupons are not private"
                return return_code_400(message)
                
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = RewardProgramReadSerializer(self.instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        self.instance = serializer.save(created_by=self.request.user, updated_by=self.request.user)
        instance_winery = Winery.objects.get(account=self.request.user)
        if not(instance_winery.is_active):
            self.instance = serializer.save(is_active=False)
        
        
class RemoveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RewardProgramWriteSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    lookup_url_kwarg = 'program_id'
    
    def get_queryset(self):
        queryset = RewardProgram.objects.filter(created_by=self.request.user, deleted_by=None)
        return queryset
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        for coupon in serializer.validated_data['coupons']:
            instance_coupon = Coupon.objects.filter(code=coupon, created_by=self.request.user, is_active=True, is_public=False) 
            if not(instance_coupon.exists()):
                message = "You don't own this coupon Or Coupons are not private"
                return return_code_400(message)
            
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        serializer = RewardProgramReadSerializer(self.instance)
        return Response(serializer.data)
    
    def perform_update(self, serializer):
        self.instance = serializer.save(updated_by=self.request.user)
        instance_winery = Winery.objects.get(account=self.request.user)
        if not(instance_winery.is_active):
            self.instance = serializer.save(is_active=False)
            
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_by = self.request.user
        instance.deleted_at = timezone.now()
        instance.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)