from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView
from rest_framework_simplejwt import authentication

from rest_framework import generics, permissions, response, status

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from . import serializers
User = get_user_model()



class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = serializers.ChangePasswordSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if serializer.data.get("new_password") != serializer.data.get("confirm_password"):
                return response.Response({"message": ["New password and confirm password don't match"]}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return response.Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))            
            self.object.save()
                       
            return response.Response(status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ProfileUpdateRetrieveAPIView(generics.RetrieveUpdateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if(self.request.method == "GET"):
            self.serializer_class = serializers.ProfileSerializer
        else:
            self.serializer_class = serializers.ProfileSerializer          
        return super().get_serializer_class()
    
    def get_object(self, queryset=None):
        obj = get_object_or_404(User,id=self.request.user.id)
        return obj    


class UploadImageAPIView(generics.UpdateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ImageSerializer

    def get_object(self, queryset=None):
        obj = get_object_or_404(User,id=self.request.user.id)
        print(obj)
        return obj    
