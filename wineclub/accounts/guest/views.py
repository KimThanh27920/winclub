import random
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from .serializers import ChangePasswordWithPinSerializer
from .serializers import PinSerializer
from ..models import Pin
# Create your views here.
User = get_user_model()


class LoginApiView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


# class ForgotPasswordApiView(APIView):

#     def create_pin(self, user):
#         pin = random.randint(100000, 999999)
#         data = {
#             'user': user.id,
#             'pin': pin
#         }
#         pin_user = Pin.objects.filter(user=user.id)
#         if(pin_user.exists()):
#             serializer = PinSerializer(instance=pin_user[0], data=data)
#         else:
#             serializer = PinSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return pin

#     def post(self, request):
#         user = get_object_or_404(User, email=request.data["email"].lower())
#         pin_code = self.create_pin(user)
#         html_content = render_to_string(
#             "index.html", {'fullname': "USER", 'pin': pin_code})
#         send_mail(
#             subject='WineClub - Forgot Password',
#             message='PIN',
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[request.data["email"]],
#             html_message=html_content
#         )
#         return Response({"message": "Send email completed"}, status=status.HTTP_200_OK)


# class ChangePasswordWithPINApiView(APIView):

#     def disable_pin(self):
#         self.pin.delete()

#     def post(self, request):

#         serializers = ChangePasswordWithPinSerializer(data=request.data)
#         serializers.is_valid(raise_exception=True)
#         self.user = get_object_or_404(
#             User, email=request.data['email'].lower())
#         self.pin = get_object_or_404(Pin, user=self.user.id)

#         if int(request.data['pin']) == int(self.pin.pin):
#             self.user.set_password(request.data['new_password'])
#             self.user.save()
#             self.disable_pin()
#             return Response(data={"message": "Change password is success"}, status=status.HTTP_200_OK)
#         else:
#             return Response(data={"message": "Is valid PIN code"}, status=status.HTTP_400_BAD_REQUEST)
