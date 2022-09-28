from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView
from rest_framework_simplejwt import authentication

from rest_framework import generics, permissions, response, status, views

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from . import serializers
from wineries.models import Winery
from bases.services.stripe.stripe import stripe_created_account_link
class StripeConnectRegistration(views.APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        instance = Winery.objects.get(account = self.request.user)
        link = stripe_created_account_link(instance.account_connect)
        
        return response.Response(
            data={
                "url": link.url
            },
            status=status.HTTP_200_OK
        )