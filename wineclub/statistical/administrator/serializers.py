#rest framework import
from rest_framework import serializers
# App imports
from wineries.models import Winery

#Wine Serializer in Top Wine
class WineryInTopSerializer(serializers.ModelSerializer):


    class Meta:
        model=Winery
        fields =[ 
            'id',
            'name'
        ]
        read_only_fields = ['id','name']

#Top Winery Products
class TopWineryProductsSerializer(serializers.ModelSerializer):
    products = serializers.IntegerField()
    winery = serializers.SerializerMethodField()

    class Meta:
        model = Winery
        fields = [
            'winery',
            'products',
            
        ]
        read_only_fields = ['winery','products']

    def get_winery(self, obj):
            winery = int(obj["id"])
            query = Winery.objects.get(id=winery)
            serializer = WineryInTopSerializer(query)
            return serializer.data


#Top Winery
class TopWineryRevenueSerializer(serializers.ModelSerializer):
    revenues = serializers.IntegerField()
    winery = serializers.SerializerMethodField()

    class Meta:
        model = Winery
        fields = [
            'winery',
            'revenues',
            
        ]
        read_only_fields = ['winery','revenues']

    def get_winery(self, obj):
            winery = int(obj["id"])
            query = Winery.objects.get(id=winery)
            serializer = WineryInTopSerializer(query)
            return serializer.data


#Top Winery Transactions
class TopWineryTransSerializer(serializers.ModelSerializer):
    transaction = serializers.IntegerField()
    winery = serializers.SerializerMethodField()

    class Meta:
        model = Winery
        fields = [
            'winery',
            'transaction'
            
        ]
        read_only_fields = ['winery','transaction']

    def get_winery(self, obj):
            winery = int(obj["winery"])
            query = Winery.objects.get(id=winery)
            serializer = WineryInTopSerializer(query)
            return serializer.data