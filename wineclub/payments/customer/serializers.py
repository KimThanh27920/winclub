from rest_framework import serializers


class ListPaymentMethodSerializer(serializers.Serializer):
    id = serializers.CharField()
    brand = serializers.CharField()
    exp_month = serializers.IntegerField()
    exp_year = serializers.IntegerField()
    last4 = serializers.IntegerField()