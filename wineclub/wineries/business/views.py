# From django
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
# From rest_framework
from rest_framework_simplejwt import authentication
from rest_framework import generics, permissions
# From app
from .serializers import WineryUploadImageCoverSerializer, WineryProfileSerializer
from ..models import Winery

User = get_user_model()



class BusinessProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = WineryProfileSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, queryset=None):
        obj = get_object_or_404(Winery,account=self.request.user.id)
        
        return obj    


class UploadImageCover(generics.UpdateAPIView):
    serializer_class = WineryUploadImageCoverSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]    
   
    def get_object(self, queryset=None):
        obj = get_object_or_404(Winery,account=self.request.user.id)
        
        return obj    
