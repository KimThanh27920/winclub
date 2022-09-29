from rest_framework_simplejwt import authentication
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from . import serializers
from orders.models import Order
from wineries.models import Winery
from wines.models import Wine

from django.core.mail import send_mail
from django.conf import settings

class ListOrderBusinessAPIView(generics.ListCreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.OrderSerializer
        else:
            return serializers.ListOrderSerializer

    def get_queryset(self):
        winery = Winery.objects.get(id=self.request.user.id)
        self.queryset = Order.objects.filter(winery=winery)

        search = self.request.query_params.get('search')

        if search:
            self.queryset = Order.objects.filter(winery=winery, full_name__icontains=search)

        return super().get_queryset()

    def post(self, request, *args, **kwargs):
        serializer = serializers.OrderSerializer(data=request.data.get('order'))
        order_detail_arr = self.request.data.get('order_details')

        if serializer.is_valid():
            self.instance = serializer.save(created_by=self.request.user, updated_by=self.request.user)
            instance_price = 0

            for order_detail in order_detail_arr:
                wine = Wine.objects.get(id=order_detail.get('wine'))
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

            self.instance.total = instance_price
            self.instance.status = "completed"
            self.instance.payment = "charged"
            self.instance.save()
            serializer = serializers.OrderSerializer(self.instance)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailOrderBusinessAPIView(generics.RetrieveUpdateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'order_id'

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return serializers.UpdateOrderStatusSerializer
        else:
            return serializers.DetailOrderSerializer

    def get_queryset(self):
        winery = Winery.objects.get(id=self.request.user.id)
        self.queryset = Order.objects.filter(winery=winery)
        return super().get_queryset()

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        status_update = self.request.data.get('status')
        order.status = status_update
        order.save()

        title_mail = 'UPDATE ORDER STATUS, ORDER ID: "'+str(order.id)+'"'
        message = "My Order Status updated is "+ order.status
        send_mail(title_mail, message, settings.EMAIL_HOST_USER, ['huudang0206@gmail.com'], fail_silently=False)
        return super().update(request, *args, **kwargs)