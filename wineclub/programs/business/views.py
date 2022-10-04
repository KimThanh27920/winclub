# From rest_framework
from rest_framework import generics, permissions, status, filters
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
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    pagination_class = None
    filter_backends = [filters.OrderingFilter]
    ordering = ['-created_at']
    
    def get_queryset(self):
        self.queryset = RewardProgram.objects.filter(created_by=self.request.user.id)
        return self.queryset
    
    def get_serializer_class(self):
        if(self.request.method == "POST"):
            self.serializer_class = RewardProgramWriteSerializer
            return self.serializer_class
        
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        for coupon in serializer.validated_data['coupons']:
            instance_coupon = Coupon.objects.filter(code=coupon, created_by=self.request.user) 
            if not(instance_coupon.exists()):
                message = "You don't own this coupon"
                return return_code_400(message)
                
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # serializer = RewardProgramReadSerializer(data=serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)
        
        
class RemoveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RewardProgramWriteSerializer
    queryset = RewardProgram.objects.all()
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    lookup_url_kwarg = 'program_id'