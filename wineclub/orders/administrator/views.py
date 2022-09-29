from rest_framework_simplejwt import authentication
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from . import serializers
from orders.models import Order


class ListOrderAdminAPIView(generics.ListAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.ListOrderAdminSerializer

    def get_queryset(self):
        self.queryset = Order.objects.all()
        return super().get_queryset()


class RetrieveOrderAdminAPIView(generics.RetrieveAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]
    lookup_url_kwarg = 'order_id'
    queryset = Order.objects.all()
    serializer_class = serializers.OrderDetailAdminSerializer