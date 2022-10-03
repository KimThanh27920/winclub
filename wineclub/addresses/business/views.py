# From rest_framework
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt import authentication
# From app
from bases.permissions.business import IsBusiness
from bases.errors.addresses import check_address_business_exist
from . import serializers
from .. import models



class ListCreateBusinessAddressAPI(generics.ListCreateAPIView):    
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    serializer_class = serializers.AddressSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = models.Address.objects.filter(account_id=self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):
        error = check_address_business_exist(self.request.user.id) #Business only has a address
        if(error is not None):
            return error
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):        
        serializer.save(account = self.request.user)


class RetrieveUpdateDestroyBusinessAddressAPI(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    serializer_class = serializers.AddressSerializer
    lookup_url_kwarg = "address_id"

    def get_queryset(self):
        queryset = models.Address.objects.filter(account_id=self.request.user.id)
        return queryset

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


    