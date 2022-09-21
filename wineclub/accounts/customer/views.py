<<<<<<< HEAD
from rest_framework import generics, permissions, response, status

from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView
from rest_framework_simplejwt import tokens, authentication

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
    
    # def get_object(self, queryset=None):
    #     obj = get_object_or_404(User,id=self.request.user.id)
    #     return obj    
    
    # def perform_update(self, serializer):
    #     serializer.save(updated_by=self.request.user.id)
=======
import random

from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt import tokens

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from .serializers import MyTokenObtainPairSerializer


# Create your views here.
User = get_user_model()


class LoginApiView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        request.data['email'] = request.data.get('email').lower()
        return super().post(request, *args, **kwargs)
>>>>>>> 5e904269ef05ed4b928ad685f88064f2ab78ff2c
