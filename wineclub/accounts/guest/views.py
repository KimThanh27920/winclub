import random
from datetime import datetime
from venv import create
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import PinSerializer
from .serializers import RegisterSerializer
from .serializers import ForgotPasswordSerializer
from .serializers import BusinessRegisterSerializer
from .serializers import MyTokenObtainPairSerializer
from .serializers import ChangePasswordWithPinSerializer
from ..models import Pin
from bases.services.stripe.stripe import stripe_customer_create
User = get_user_model()


class LoginApiView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        """
        create stripe customer when user register
        will put this function on the task in celery
        """
        customer_stripe = stripe_customer_create(instance)
        instance.stripe_account = customer_stripe
        instance.save()


class BusinessRegisterAPI(generics.CreateAPIView):
    serializer_class = BusinessRegisterSerializer

    def perform_create(self, serializer):
        instance = serializer.save(is_business=True)

        """
        create stripe customer when user register
        maybe put this function on the task in celery
        """
        customer_stripe = stripe_customer_create(instance)
        instance.stripe_account = customer_stripe
        instance.save()


class ForgotPasswordApiView(APIView):
    def create_pin(self, user):
        pin = random.randint(100000, 999999)
        dt = datetime.now()
        ts = int(datetime.timestamp(dt))
        expired = ts + (60 * 10)
        data = {
            'user': user.id,
            'pin': pin,
            'expired': expired
        }
        pin_user = Pin.objects.filter(user=user.id)
        if(pin_user.exists()):
            serializer = PinSerializer(instance=pin_user[0], data=data)
        else:
            serializer = PinSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return pin

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, email=request.data["email"].lower())
        pin_code = self.create_pin(user)
        html_content = render_to_string(
            "index.html", {'fullname': "USER", 'pin': pin_code})
        send_mail(
            subject='WineClub - Forgot Password',
            message='PIN',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.data["email"]],
            html_message=html_content
        )
        return Response({"message": "Send email completed"}, status=status.HTTP_200_OK)


class ChangePasswordWithPINApiView(APIView):

    def disable_pin(self):
        self.pin.delete()

    def post(self, request):
        serializers = ChangePasswordWithPinSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        self.user = get_object_or_404(
            User, email=request.data['email'].lower())
        self.pin = get_object_or_404(Pin, user=self.user.id)

        """
        check if the user's PIN code input pin is correct
        and check expired PIN code
        """

        dt = datetime.now()
        ts = int(datetime.timestamp(dt))

        if (int(request.data['pin']) == int(self.pin.pin) and int(self.pin.expired) > ts):
            self.user.set_password(request.data['new_password'])
            self.user.save()
            self.disable_pin()
            return Response(data={"detail": "Change password is success"}, status=status.HTTP_200_OK)
        else:
            return Response(data={"detail": "Is valid PIN code or expired"}, status=status.HTTP_400_BAD_REQUEST)
