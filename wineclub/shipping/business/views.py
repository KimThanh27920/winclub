from rest_framework_simplejwt import authentication
from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response

from .serializers import ShippingUnitSerializer, ShippingUnitDetailSerializer, UpdateShippingUnitBusinessSerializer
from shipping.models import ShippingBusinessService, ShippingUnit
from wines.models import Winery


class ShippingUnitWineryViewSet(viewsets.ViewSet, generics.ListAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ShippingUnitSerializer

    def get_queryset(self):
        winery = Winery.objects.get(account=self.request.user)
        shipping_business = ShippingBusinessService.objects.filter(winery=winery)

        return shipping_business


class ManageShippingUnitWineryViewSet(viewsets.ViewSet, generics.CreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def create(self, request, *args, **kwargs):
        try:

            shipping_services_arr = self.request.data.get("shipping_services")
            arr = []
            winery = Winery.objects.get(account=self.request.user)
            for shipping_service in shipping_services_arr:
                s = ShippingUnit.objects.get(id=shipping_service.get('id'))
                arr.append(s)

            data = {
                "shipping_services": arr
            }
            serializer = ShippingUnitDetailSerializer(data=data)
            serializer.is_valid()
            serializer.save(winery= winery,
                            shipping_services=arr,
                            created_by=self.request.user,
                            updated_by=self.request.user)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # finally:
        #     winery = Winery.objects.get(account=self.request.user)
        #     shipping_business = ShippingBusinessService.objects.filter(winery=winery)
        #     serializer = ShippingUnitDetailSerializer(data=shipping_business)
        #     serializer.is_valid()

        #     print(shipping_business[0].__dict__)

        #     return Response(serializer.data)
        
