# From rest_framework
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt import authentication
# From app
from bases.permissions.business import IsBusiness
from bases.errors.bases import return_code_400
from coupons.models import Coupon
from .serializers import RewardProgramWriteSerializer, RewardProgramReadSerializer
from ..models import RewardProgram



class ProgramListCreateView(generics.ListCreateAPIView):
    serializer_class = RewardProgramReadSerializer
    queryset = RewardProgram.objects.all()
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    
    def get_serializer_class(self):
        if(self.request.method == "POST"):
            self.serializer_class = RewardProgramWriteSerializer
            return self.serializer_class
        
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(serializer.validated_data['coupons'])
        for coupon in serializer.validated_data['coupons']:
            instance_coupon = Coupon.objects.filter(code=coupon, created_by=self.request.user) 
            if not(instance_coupon.exists()):
                message = "You don't own this coupon"
                return return_code_400(message)
                
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)