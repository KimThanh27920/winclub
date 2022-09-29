from rest_framework import generics, status, permissions
from rest_framework_simplejwt import authentication
from rest_framework.response import Response

from bases.permissions.rolecheck import IsOwnerByAccount
from .serializers import CouponOwnerReadSerializer, CouponListSerializer, CouponDetailSerializer
from ..models import CouponOwner



class CouponOwnerCreateListView(generics.ListCreateAPIView):
    serializer_class = CouponListSerializer
    queryset = CouponOwner.objects.all()
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
   
    # def get_queryset(self):
    #     self.queryset = queryset = CouponOwner.objects.filter(account=self.request.user.id)
    #     return super().get_queryset()
    
    def get_serializer_class(self):
        if(self.request.method == "GET"):
            self.serializer_class = CouponOwnerReadSerializer
        
        return super().get_serializer_class()
    
    def get_object(self, queryset=None):
        obj = CouponOwner.objects.filter(account=self.request.user.id)
        self.check_object_permissions(self.request, obj[0])
        return obj[0]
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        obj_coupon = instance.coupons.filter(id=self.request.data.get("coupon_id"))
        if (obj_coupon.exists()):
            return Response(data={"message": "You have been added this coupon"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            instance.coupons.add(self.request.data.get("coupon_id"))
                     
        instance.save()        
        serializer = self.get_serializer(instance.coupons.last())       
           
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class CouponRemoveView(generics.RetrieveDestroyAPIView):
    serializer_class = CouponDetailSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = "coupon_id"
    
    def get_object(self):
        obj = CouponOwner.objects.get(account=self.request.user.id)
        return obj
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        coupon_id = self.kwargs['coupon_id']
        instance.coupons.remove(coupon_id)
        instance.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)