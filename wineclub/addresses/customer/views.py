# from rest_framework import status
# from rest_framework import generics
# from rest_framework import permissions
# from rest_framework.response import Response

# from rest_framework_simplejwt import authentication

# from . import serializers
# from .. import models


# class ListCreateCustomerAddressAPI(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [authentication.JWTAuthentication]
#     serializer_class = serializers.DeliverySerializer
#     queryset = models.Delivery.objects.all()

#     def get_object(self):
#         return super().get_object()

#     def create_address(self):
#         serializer = serializers.AddressSerializer(
#             data=self.request.data['address'])
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return serializer.data

#     def create_delivery(self):
#         address = self.create_address()
#         address_instance = models.Address.objects.get(id=address['id'])
#         serializer = serializers.CreateDeliverySerializer(
#             data=self.request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(address=address_instance, created_by=self.request.user)
#         return serializer.data

#     def get_queryset(self):
#         queryset = models.Delivery.objects.filter(
#             created_by=self.request.user.id)
#         return queryset

#     def create(self, request, *args, **kwargs):
#         serializer = serializers.DeliverySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         delivery_instance = self.create_delivery()
#         queryset = models.Delivery.objects.get(id=delivery_instance['id'])
#         serializer = serializers.DeliverySerializer(queryset)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class RetrieveUpdateDestroyCustomerAddressAPI(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [authentication.JWTAuthentication]
#     serializer_class = serializers.DeliverySerializer
#     lookup_url_kwarg = "address_id"

#     def get_queryset(self):
#         queryset = models.Delivery.objects.filter(
#             created_by=self.request.user.id)
#         return queryset


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


    