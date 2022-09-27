from rest_framework_simplejwt import authentication
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Account

import stripe

stripe.api_key = "sk_test_51LXILOJvtSsB9DmY807yqCiAQ3EzpKLd62eSU2G9AmbYiSTnGv8MN7Eb368nRPmD3sw2SEkJdYZZZ7mImkgn3I5T00Br7ykapJ"

class PaymentMethodAPIView(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        customer = Account.objects.get(email=self.request.user)
        
        list_pm_customer = stripe.Customer.list_payment_methods(
            customer.stripe_account,
            type="card",
        )
        return Response({"Info_Card": list_pm_customer["data"]},
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
            return Response({"error": "Not Found Card Or Card Deleted"},
                            status=status.HTTP_400_BAD_REQUEST)