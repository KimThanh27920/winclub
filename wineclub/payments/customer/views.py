from rest_framework_simplejwt import authentication
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from accounts.models import Account
from .serializers import ListPaymentMethodSerializer

import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentMethodAPIView(generics.ListCreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListPaymentMethodSerializer

    def get(self, request):
        customer = Account.objects.get(email=self.request.user)
        
        list_pm_customer = stripe.Customer.list_payment_methods(
            customer.stripe_account,
            type="card",
        )
        data = []
        for pm in list_pm_customer["data"]:
            pm_list = {
                "id": pm["id"],
                "brand": pm["card"]["brand"],
                "exp_month": pm["card"]["exp_month"],
                "exp_year": pm["card"]["exp_year"],
                "last4": pm["card"]["last4"]
            }
            data.append(pm_list)
            
        serializer = ListPaymentMethodSerializer(data=data, many=True)
        serializer.is_valid()

        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def post(self, request):

        customer = Account.objects.get(email=self.request.user)
        try:
            setup_intent = stripe.SetupIntent.create(
                payment_method_types = ["card"],
                customer = customer.stripe_account,
            )

            return Response({'setup_id': setup_intent["id"],
                            'client_secret': setup_intent["client_secret"]},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

                    
class DeletePaymentMethodAPIView(generics.DestroyAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pm_id):
        customer = Account.objects.get(email=self.request.user)
        try:
            stripe.Customer.delete_source(
                customer.stripe_account,
                pm_id
            )

            return Response({"Notification": "Delete PaymentMethod Succeed"},
                            status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)