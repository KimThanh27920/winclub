import email
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from bases.exception.exceptions import response_exception
from bases.services.stripe.stripe import stripe_webhook
from bases.services.stripe.webhook import update_account
# Create your views here.





class StipeWebhookAPI(APIView):

    def post(self, request):
        event = stripe_webhook(request)
        if(type(event).__name__ == "SignatureVerificationError"):
            return response_exception(event)
        if event.type == 'invoice.payment_succeeded':
            print(event)
        return Response()
