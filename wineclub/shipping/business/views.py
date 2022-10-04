from rest_framework_simplejwt import authentication
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from . import serializers
from shipping.models import ShippingBusinessService, ShippingUnit
from wines.models import Winery

from bases.permissions.business import IsBusiness

class ShippingUnitWineryAPIView(generics.ListAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    serializer_class = serializers.ShippingUnitBusinessSerializer

    def get_queryset(self):
        winery = Winery.objects.get(account=self.request.user)
        shipping_business = ShippingBusinessService.objects.filter(winery=winery)

        return shipping_business


class AddShippingUnitBusinessAPIView(generics.CreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AddShippingUnitSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = serializers.AddShippingUnitSerializer(data=request.data)
            shipping_arr = self.request.data.get('shipping_services')
            winery = Winery.objects.get(account=self.request.user)
            if serializer.is_valid():
                self.instance = serializer.save(winery=winery, created_by=self.request.user, updated_by=self.request.user)

                for shipping in shipping_arr:
                    shipping_unit = ShippingUnit.objects.get(id=shipping.get('id'))
                    self.instance.shipping_services.add(shipping_unit)
                    self.instance.save()

                serializer = serializers.AddShippingUnitSerializer(self.instance)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        finally:
            try:
                winery = Winery.objects.get(account=self.request.user)
                shipping_service = ShippingBusinessService.objects.filter(winery=winery)
                shipping_arr = self.request.data.get('shipping_services')

                for shipping in shipping_arr:
                    shipping_unit = ShippingUnit.objects.get(id=shipping.get('id'))
                    shipping_service[0].shipping_services.add(shipping_unit)
                    shipping_service[0].save()
                
                return Response({"Notify":"Add Shipping Unit Is successfuly"},status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class RemoveShippingUnitAPIView(generics.CreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AddShippingUnitSerializer

    def post(self, request, *args, **kwargs):
        try:
            winery = Winery.objects.get(account=self.request.user)
            shipping_service = ShippingBusinessService.objects.filter(winery=winery)
            shipping_arr = self.request.data.get('shipping_services')

            for shipping in shipping_arr:
                shipping_unit = ShippingUnit.objects.get(id=shipping.get('id'))
                shipping_service[0].shipping_services.remove(shipping_unit)
                shipping_service[0].save()
            
            return Response({"Notify":"Remove Shipping Unit Is successfuly"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
