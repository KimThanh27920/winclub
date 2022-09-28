
from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "timestamp",
            "type",
            "amount",
            "currency",
            "net",
            "fee",
            "unit",
            "description",
            "sender",
            "receiver",
        ]
