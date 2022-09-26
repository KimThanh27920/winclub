from rest_framework_simplejwt import authentication
from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response
from .serializers import ShippingUnitSerializer, UpdateStatusShippingUnitSerializer
from shipping.models import ShippingUnit


class ShippingUnitViewSet(viewsets.ViewSet, generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdateStatusShippingUnitSerializer
        else:
            return ShippingUnitSerializer

    def get_queryset(self):
        shipping_unit = ShippingUnit.objects.all().order_by("-id")
        return shipping_unit

    def create(self, request, *args, **kwargs):
        data = self.request.data
        try:
            serializer = ShippingUnitSerializer(data=data)

            if serializer.is_valid():
                serializer.save(created_by=self.request.user, updated_by=self.request.user)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        shipping_unit = self.get_object()
        shipping_unit.is_active = not shipping_unit.is_active
        shipping_unit.save()
        return super().update(request, *args, **kwargs)


