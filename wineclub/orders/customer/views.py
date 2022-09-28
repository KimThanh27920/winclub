from rest_framework_simplejwt import authentication
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from . import serializers
from wines.models import Wine
from accounts.models import Account
from wineries.models import Winery
from carts.models import CartDetail, Cart
from orders.models import Order


class OrderAPIView(generics.ListCreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        order_list = Order.objects.filter(created_by=self.request.user.id)
        return order_list

    def post(self, request, *args, **kwargs):
        serializer = serializers.OrderSerializer(data=request.data.get('order'))
        order_detail_id = self.request.data.get('cart')

        cart = Cart.objects.get(id=order_detail_id)

        order_details = CartDetail.objects.filter(cart=order_detail_id)

        winery = Winery.objects.get(id=cart.winery_id)

        if serializer.is_valid():
            self.instance = serializer.save(created_by=self.request.user, updated_by=self.request.user, winery=winery)
            instance_price = 0

            for order_detail in order_details:
                wine = Wine.objects.get(id=order_detail.wine_id)
                if wine.sale > 0:
                    price = wine.sale
                else:
                    price = wine.price
                
                instance_price += float(price) * int(order_detail.quantity)

                data = {
                    "order": self.instance.id,
                    "price": price,
                    "sale": wine.sale,
                    "wine": wine.id,
                    "quantity": order_detail.quantity
                }
                serializer = serializers.OrderDetailSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
            
            if self.instance.used_points == True:
                account = Account.objects.get(id=self.request.user.id)
                instance_price -= account.points
                account.points = 0
                account.save()
            
            try:
                self.instance.total = instance_price
                self.instance.save()

                serializer = serializers.OrderSerializer(self.instance)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateOrderAPIView(generics.RetrieveUpdateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'order_id' 
    
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return serializers.UpdateOrderStatusSerializer
        else:
            return serializers.ListOrderSerializer

    def get_queryset(self):
        self.queryset = Order.objects.filter(created_by=self.request.user.id)
        return super().get_queryset()

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        order.status = "canceled"
        order.save()

        return super().update(request, *args, **kwargs)