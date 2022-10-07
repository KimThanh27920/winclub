from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView
from rest_framework_simplejwt import authentication

from rest_framework import generics, permissions, response, status, views

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from . import serializers
from wineries.models import Winery
from bases.services.stripe.stripe import stripe_created_account_link
from bases.services.stripe.stripe import stripe_retrieve_account
from bases.services.stripe.stripe import stripe_created_connect
from . import serializers


class StripeConnectRegistration(views.APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        instance = Winery.objects.get(account=self.request.user)
        link = stripe_created_account_link(instance.account_connect)

        return response.Response(
            data={
                "url": link.url
            },
            status=status.HTTP_200_OK
        )


class RetrieveConnectAPI(views.APIView):

    def get(self, request, *args, **kwargs):

        data = stripe_retrieve_account("acct_1LoehMIxYV2lliw7")
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip)

        return response.Response(data=data)


class RegisterConnectAccountAPI(views.APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = serializers.ConnectAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        stripe_connect = stripe_created_connect(
            self.request.user.email,
            self.request.data["address_business"],
            self.request.data["identity_verify"],
            self.request.data["business_profile"],
            self.request.data["bank_account"]
        )
        return response.Response(
            data={
                "message": "create stripe connect account success"
            }
        )