#rest framework import
from rest_framework import serializers
# App imports
from wines.models import Wine
from orders.models import Order
from accounts.models import Account

#Wine Serializer in Top Wine
class WineInTopSerializer(serializers.ModelSerializer):


    class Meta:
        model=Wine
        fields =[ 
            'id',
            'wine'
        ]
        read_only_fields = ['id','wine']

#Top Wine
class TopWineSerializer(serializers.ModelSerializer):
    solds = serializers.IntegerField()
    wine = serializers.SerializerMethodField()

    class Meta:
        model = Wine
        fields = [
            'wine',
            'solds'
        ]
        read_only_fields = ['wine','solds']

    def get_wine(self, obj):
            wine = int(obj['wine'])
            query = Wine.objects.get(id=wine)
            serializer = WineInTopSerializer(query)
            return serializer.data


#customer serializer in top
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields =[ 
            'id',
            'full_name',
            'email'
        ]

#Top Customer 
class TopCustomerSerializer(serializers.ModelSerializer):
    buys = serializers.FloatField()
    customer = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'customer',
            'buys',  
        ]

    def get_customer(self, obj):
            user = int(obj['created_by'])
            query = Account.objects.get(id=user)
            serializer = CustomerSerializer(query)
            return serializer.data
