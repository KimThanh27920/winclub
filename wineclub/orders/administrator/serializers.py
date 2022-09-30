from rest_framework import serializers
from orders.models import Order, OrderDetail


class ListOrderAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            "id",
            "full_name",
            "phone",
            "created_at",
            "winery",
            "status"
        ]


class ReadOnlyOrderDetailAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = [
            "id",
            "wine",
            "price",
            "sale",
            "quantity"
        ]


class OrderDetailAdminSerializer(serializers.ModelSerializer):
    order_detail = ReadOnlyOrderDetailAdminSerializer(many=True)
    class Meta:
        model = Order
        fields = [
            "id",
            "full_name",
            "phone",
            "created_at",
            "total",
            "winery",
            "order_detail"
        ]