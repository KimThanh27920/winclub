from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework_simplejwt import authentication

from . import serializers
from .. import models


class ListCreateCustomerAddressAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.AddressSerializer

    def get_queryset(self):
        queryset = models.Address.objects.filter(
            account_id=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        if(self.request.data['is_default']):
            queryset_address = models.Address.objects.filter(
                account_id=self.request.user.id)
            for obj in queryset_address:
                obj.is_default = False
                obj.save()
        serializer.save(account=self.request.user)


class RetrieveUpdateDestroyCustomerAddressAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.AddressSerializer
    lookup_url_kwarg = "address_id"

    def get_queryset(self):
        queryset = models.Address.objects.filter(
            account_id=self.request.user.id)
        return queryset

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        if(self.request.data['is_default']):
            queryset_address = models.Address.objects.filter(
                account_id=self.request.user.id)
            for obj in queryset_address:
                obj.is_default = False
                obj.save()
        serializer.save(account=self.request.user)

#     def update(self, request, *args, **kwargs):
#         # update info delivery
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # update address
#         address = models.Address.objects.get(id = request.data['address']['id'])
#         serializer_address = serializers.AddressSerializer(address, data=request.data['address'], partial=True)
#         serializer_address.is_valid(raise_exception=True)
#         serializer_address.save()
#         return Response(serializer.data)
