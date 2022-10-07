# Rest framework imports
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
#Django import
from django.db.models import Count, Sum
from django.utils import timezone
# App imports
from wineries.models import Winery
from orders.models import Order
from wines.models import Wine
from accounts.models import Account
from transactions.models import Transaction
from orders.models import Order
from .serializers import  TopWineryProductsSerializer, TopWineryRevenueSerializer


#Statistical of Admin
class AdminStatistical(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self, request, *args, **kwargs):
        # winery statistic
        total_wineries = Winery.objects.exclude(deleted_at__isnull=False).count()

        # order statistic
        total_order = Order.objects.all().exclude(deleted_at__isnull=False).count()
        order_success = Order.objects.filter(status="completed").filter(payment="charged").exclude(deleted_at__isnull=False).count()

        if(total_order != 0):
            order_rate = (order_success/total_order)*100
        else:
            order_rate = 0

        #product statistic
        total_product = Wine.objects.all().exclude(deleted_at__isnull=False).count()

        #customer statistics
        total_customer = Account.objects.filter(is_business=False).filter(is_superuser=False).count()

        #transaction statistic
        total_trans = Transaction.objects.all().count()

        #total revenue
        now_month=timezone.now().month

        #Best business
        wineries = Winery.objects.filter(is_active=True)
        
        product_of_winery = Winery.objects.prefetch_related("origin").filter(is_active=True).values('id').annotate(
            products=Count("origin__id")).order_by("products")
        
        winery_products_serializer = TopWineryProductsSerializer(product_of_winery, many=True)
        
        revenues = Winery.objects.filter(is_active=True).prefetch_related("winery").values('id').annotate(
            revenues=Sum("winery__total")).order_by("revenues")
        
        winery_revenues_serializer = TopWineryRevenueSerializer(revenues, many=True)


        revenue = Transaction.objects.filter(receiver="Platform").filter(type="charge").filter(timestamp__year=now_month).annotate(revenue=Sum("amount"))

     
        data = {
            "revenue": revenue.revenue,
            "wineries": total_wineries,
            "order": total_order,
            "product": total_product,
            "customer": total_customer,
            "transactions": total_trans,
            "order_success_rate": order_rate,
            # "top_trans_winery":winery_trans_serializer.data,
            "top_products_winery": winery_products_serializer.data,
            "top_revenue_winery": winery_revenues_serializer.data   


        }

        return Response(data = data,status=status.HTTP_200_OK)