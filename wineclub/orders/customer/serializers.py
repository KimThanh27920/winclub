from rest_framework import serializers
from orders.models import Order, OrderDetail
from wines.models import Wine


class ReadWineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wine
        fields = [
            "id",
            "price",
            "sale",
            "winery"
        ]


class OrderDetailReadOnlySerializer(serializers.ModelSerializer):
    wine = ReadWineSerializer(read_only = True)
    class Meta:
        model = OrderDetail
        fields = [
            "id",
            "price",
            "sale",
            "wine",
            "quantity" 
        ]
        extra_kwargs = {
            'order': {'write_only': True},
        }


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = [
            "order",
            "price",
            "sale",
            "wine",
            "quantity" 
        ]
        extra_kwargs = {
            'order': {'write_only': True},
        }


class OrderSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailReadOnlySerializer(many = True, read_only = True)
    class Meta:
        model = Order
        fields = [
            "id",
            "winery",
            "shipping_service",
            # "coupons",
            "note",
            "used_points",
            "total",
            "status",
            "payment",
            "address",
            "full_name",
            "phone",
            "order_detail",
        ]
        read_only_fields = ['winery']


class ListOrderDetailReadOnlySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderDetail
        fields = [
            "id",
            "wine",
            "price",
            "sale",
            "quantity"
        ]

    
class ListOrderSerializer(serializers.ModelSerializer):
    order_detail = ListOrderDetailReadOnlySerializer(many=True)
    class Meta:
        model = Order
        fields = [
            "id",
            "winery",
            "shipping_service",
            "note",
            "used_points",
            "total",
            "status",
            "payment",
            "address",
            "full_name",
            "phone",
            "order_detail",
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
        ]


class UpdateOrderStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            "status"
        ]