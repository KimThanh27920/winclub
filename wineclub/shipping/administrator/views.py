from rest_framework_simplejwt import authentication
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from . import serializers
from shipping.models import ShippingUnit


class ShippingUnitAPIView(generics.ListCreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.ShippingUnitSerializer

    def get_queryset(self):
        shipping_unit = ShippingUnit.objects.all().order_by("-id")

        search = self.request.query_params.get('search')
        
        if search:
            shipping_unit = ShippingUnit.objects.filter(name__icontains=search)
        return shipping_unit

    def post(self, request, *args, **kwargs):
        try:
            data = self.request.data
            serializer = serializers.ShippingUnitSerializer(data=data)
            if serializer.is_valid():
                serializer.save(created_by=self.request.user, updated_by=self.request.user)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteShippingUnitAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.UpdateStatusShippingUnitSerializer
    lookup_url_kwarg = 'shippingunit_id'

    def get_queryset(self):
        self.queryset = ShippingUnit.objects.all()
        return super().get_queryset()

    def update(self, request, *args, **kwargs):
        shipping_unit = self.get_object()
        shipping_unit.is_active = not shipping_unit.is_active
        shipping_unit.save()
        return super().update(request, *args, **kwargs)