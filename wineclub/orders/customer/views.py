from rest_framework_simplejwt import authentication
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from . import serializers
from wines.models import Wine
from accounts.models import Account
from orders.models import Order
from coupons.models import Coupon

import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class OrderAPIView(generics.ListCreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        order_list = Order.objects.filter(created_by=self.request.user.id)
        return order_list

    def post(self, request, *args, **kwargs):
        serializer = serializers.OrderSerializer(
            data=request.data.get('order'))
        order_detail_arr = self.request.data.get('order_details')
        coupons_arr = self.request.data.get('coupons')

        account = Account.objects.get(id=self.request.user.id)

        if serializer.is_valid():
            self.instance = serializer.save(
                created_by=self.request.user, updated_by=self.request.user)
            instance_price = 0

            for order_detail in order_detail_arr:
                wine = Wine.objects.get(id=order_detail.get('wine'))
                if wine.is_active == True:
                    if wine.sale > 0:
                        price = wine.sale
                    else:
                        price = wine.price
                    
                    instance_price += float(price) * int(order_detail.get('quantity'))

                    data = {
                        "order": self.instance.id,
                        "price": price,
                        "sale": wine.sale,
                        "wine": order_detail.get('wine'),
                        "quantity": order_detail.get('quantity')
                    }
                    serializer = serializers.OrderDetailSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
            
            for coupon in coupons_arr:
                coupons = Coupon.objects.get(id=coupon.get('id'))
                if int(coupons.coupon_value) > int(instance_price):
                    instance_price = 1
                else:
                    instance_price -= coupons.coupon_value

            if instance_price > 1:
                if self.instance.used_points == True:
                    instance_price -= account.points
                    account.points = abs(instance_price)
                    account.save()

            try:
                self.instance.total = instance_price
                self.instance.save()

                serializer = serializers.OrderSerializer(self.instance)
                
                stripe.PaymentIntent.create(
                    customer=account.stripe_account,
                    amount=int(instance_price)*100,
                    currency="aud",
                    payment_method_types=["card"],
                    metadata={
                        'customer': self.request.user,
                        'order_id': self.instance.id,
                        'winery': self.instance.winery
                    },
                    transfer_data = {
                        'destination': self.instance.winery.account_connect,
                    },
                    confirm=True,
                    payment_method=self.request.data.get('payment_method')
                )

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
