#rest framework imports
from rest_framework import serializers
# App imports
from transactions.models import Transaction
from accounts.models import Account

#Account Serializer in Transaction
class AccountTransSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields =[ 
            'id',
            'full_name',
            'email',
            'stripe_account',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'full_name': {'read_only': True},
            'email': {'read_only': True},
            'stripe_account': {'read_only': True},
        }

#Transaction serialzer for Admin
class TransactionSerializer(serializers.ModelSerializer):
    sender = AccountTransSerializer(read_only=True)
    receiver = AccountTransSerializer(read_only=True)


    class Meta:
        model = Transaction
        fields =[ 
            'id',
            'timestamp',
            'type',
            'amount',
            'currency',
            'net',
            'fee',
            'unit',
            'description',
            'sender',
            'receiver'
        ]
        
        extra_kwargs = {
            'id': {'read_only': True},
            'timestamp': {'read_only': True},
            'type': {'read_only': True},
            'amount': {'read_only': True},
            'currency': {'read_only': True},
            'net': {'read_only': True},
            'fee': {'read_only': True},
            'unit': {'read_only': True},
            'description': {'read_only': True},
            'sender': {'read_only': True},
            'receiver': {'read_only': True}
        }