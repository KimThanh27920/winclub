from rest_framework_simplejwt import authentication
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from . import serializers
from wines.models import Wine
from accounts.models import Account
from orders.models import Order
from shipping.models import ShippingBusinessService, ShippingUnit

from wines.utils import decrease_in_stock_wine
from coupons.utils import check_coupon
from bases.services.firebase import notification
import stripe
from django.conf import settings
from ..tasks import send_background_notification

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

            shipping_business = ShippingBusinessService.objects.filter(
                winery=self.instance.winery)
            shipping_unit = ShippingUnit.objects.get(
                id=self.instance.shipping_service.id)
            # Check shipping unit (in business, active)
            if shipping_unit in shipping_business[0].shipping_services.all():
                if shipping_unit.is_active == True:
                    for order_detail in order_detail_arr:
                        wine = Wine.objects.get(id=order_detail.get('wine'))
                        if wine.is_active == True:
                            if wine.in_stock >= order_detail.get('quantity'):
                                if wine.sale > 0:
                                    price = wine.sale
                                else:
                                    price = wine.price

                                instance_price += float(price) * \
                                    int(order_detail.get('quantity'))

                                decrease_in_stock_wine(
                                    wine.id, order_detail.get('quantity'))

                                data = {
                                    "order": self.instance.id,
                                    "price": price,
                                    "sale": wine.sale,
                                    "wine": order_detail.get('wine'),
                                    "quantity": order_detail.get('quantity')
                                }
                                serializer = serializers.OrderDetailSerializer(
                                    data=data)
                                if serializer.is_valid():
                                    serializer.save()
                            else:
                                return Response({"error": "The order quantity is greater than the wine product in stock"},
                                                status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return Response({"error": "Wine product not active"},
                                            status=status.HTTP_400_BAD_REQUEST)

                    # Check coupon used
                    instance_price = check_coupon(
                        coupons_arr, self.instance, instance_price)

                    # Check used point in order
                    if instance_price > 1:
                        if self.instance.used_points == True:
                            instance_price -= account.points
                            account.points = abs(instance_price)
                            account.save()

                    try:
                        self.instance.total = instance_price
                        self.instance.save()

                        serializer = serializers.OrderSerializer(self.instance)

                        # Stripe
                        stripe.PaymentIntent.create(
                            customer=account.stripe_account,
                            amount=int(instance_price)*100,
                            currency="usd",
                            payment_method_types=["card"],
                            metadata={
                                'customer': self.request.user,
                                'order_id': self.instance.id,
                                'winery': self.instance.winery
                            },
                            application_fee_amount=0,
                            transfer_data={
                                'destination': self.instance.winery.account_connect,
                            },
                            confirm=True,
                            payment_method=self.request.data.get(
                                'payment_method')
                        )
                        send_background_notification.delay(
                            self.instance.winery.account.id, "New order", "You have 1 order")
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    except Exception as e:
                        return Response({"error": str(e)},
                                        status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"error": "Shipping Unit not active"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Shipping Unit not in list shipping unit business"}, status=status.HTTP_400_BAD_REQUEST)
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
