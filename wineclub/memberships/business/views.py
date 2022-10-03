# From django
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
# From rest_framework
from rest_framework import generics, status, permissions
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
# From app
from wineries.models import Winery
from bases.permissions.business import IsBusiness
from bases.errors.bases import return_code_400
from .serializers import MembershipSerializer, MembershipCreateSerializer, AccountSerializer
from ..models import Membership


User = get_user_model()



class MembershipCreateListView(generics.ListCreateAPIView):
    serializer_class = MembershipSerializer
    queryset = Membership.objects.all()
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    pagination_class = None
    
    def get_serializer_class(self):
        if (self.request.method == "POST"):
            self.serializer_class = AccountSerializer
        
        return super().get_serializer_class()
    
    def get_object(self, queryset=None):
        instance_winery = get_object_or_404(Winery, account=self.request.user.id)
        obj = get_object_or_404(Membership, winery=instance_winery.id)
        self.check_object_permissions(self.request, obj)
        return obj
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_user = get_object_or_404(User, email=self.request.data.get("email"))
        if(instance_user.is_business or instance_user.is_staff):
            message = "User is valid"
            return return_code_400(message)
        
        obj_user = instance.users.filter(id=instance_user.id)
        if (obj_user.exists()):
            message = "You have been added this User"
            return return_code_400(message)
        
        else:
            instance.users.add(instance_user.id)
                     
        instance.save()        
        serializer = self.get_serializer(instance.users.last())       
           
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class MembershipRemoveView(generics.RetrieveDestroyAPIView):
    serializer_class = MembershipCreateSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    lookup_url_kwarg = "email"
    
    def get_object(self, queryset=None):
        instance_winery = get_object_or_404(Winery, account=self.request.user.id)
        obj = get_object_or_404(Membership, winery=instance_winery.id)
        self.check_object_permissions(self.request, obj)
        return obj
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        email = self.kwargs['email']
        instance_user = get_object_or_404(User, email=email)
        instance.users.remove(instance_user.id)
        instance.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)