# From django
from django.shortcuts import get_object_or_404
# From rest_framework
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt import authentication
# From app
from orders.models import Order
from .serializers import RewardProgramReadDetailSerializer
from ..models import RewardProgram

        
        
class RetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = RewardProgramReadDetailSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'program_id'
    
    def get_queryset(self):
        queryset = RewardProgram.objects.filter(is_active=True, deleted_by=None)
        return queryset
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        obj_order = Order.objects.filter(created_by=self.request.user, created_at__range = [instance.time_start, instance.time_end], status="completed")
        total_value = 0
        for order in obj_order.values():
            total_value += order['total']
        
        if (total_value < instance.total_price_require):
            data = {
                "message": "You are not eligible to receive the coupon"
            }
            return Response(data=data)
        
        else:
            instance.message = "You are eligible to receive the coupon"
            serializer = self.get_serializer(instance)
            
            return Response(serializer.data)