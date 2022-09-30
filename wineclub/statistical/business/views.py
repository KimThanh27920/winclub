# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
#Django import
from django.db.models import Sum, Count
# App imports
from bases.permissions.business import IsBusiness
from wineries.models import Winery
from orders.models import Order, OrderDetail
from wines.models import Wine
from memberships.models import Membership
from .serializers import TopWineSerializer, TopCustomerSerializer


#Statistical of Business
class BusinessStatistical(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsBusiness]

    def get(self, request, *args, **kwargs):
        user = self.request.user.id
        winery = Winery.objects.get(account_id = user)
        winery_id = winery.id

        # order statistic
        total_order = Order.objects.filter(winery_id=winery_id).count()
        order_processing = Order.objects.filter(winery_id=winery_id).filter(status="processing").count()
        order_processed = Order.objects.filter(winery_id=winery_id).filter(status="shipping").count()
        order_completed = Order.objects.filter(winery_id=winery_id).filter(status="completed").count()
        order_cancled = Order.objects.filter(winery_id=winery_id).filter(status="canceled").count()
        order_refund = Order.objects.filter(winery_id=winery_id).filter(payment="refund").count()
        
        #product statistic
        total_product = Wine.objects.filter(winery=winery_id).count()
        sold = Wine.objects.filter(winery=winery_id).filter(is_active=True).count()
        out_of_stock = Wine.objects.filter(winery=winery_id).filter(in_stock=0).count()

        #membership statistics
        total_member = Membership.objects.filter(winery=winery_id).count()

        #top product
        top_product = OrderDetail.objects.select_related('order').filter(order__winery=winery_id).values("wine").annotate(solds=Sum('quantity')).order_by("-solds")[:10] 
        top_wine_serializer = TopWineSerializer(top_product,many=True)
        #latest customer 
        latest_order=  Order.objects.filter(winery=winery_id).values("created_by").annotate(buys=Sum('total')).order_by("-buys")[:10] 
        latest_oredr_serializer = TopCustomerSerializer(latest_order, many=True)
      
        data = {
            "order":{
                "total": total_order,
                "processing":order_processing,
                "processed": order_processed,
                "completed":order_completed,
                "canceled":  order_cancled,
                "refund":order_refund
            },
            "product":{
                "total": total_product,
                "sold":sold,
                "out_of_stock":out_of_stock
            },

            "membership": total_member,
            "top_wine": top_wine_serializer.data,
            "top_customer": latest_oredr_serializer.data

        }

        return Response(data = data,status=status.HTTP_200_OK)