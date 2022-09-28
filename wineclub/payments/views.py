import email
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from bases.exception.exceptions import response_exception
from bases.services.stripe.stripe import stripe_webhook
from bases.services.stripe.webhook import update_account
# Create your views here.

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


def create_subscription_transaction(event):
    """
    Create transactions
    """
    data = {
        "timestamp": event.created,
        "type": "charge",
        "amount": event.data.object.amount_paid,
        "currency": event.data.object.currency,
        "net": event.data.object.amount_paid,
        "fee": 0,
        "unit": 100,
        "description": "Charge subscription " + event.data.object.lines.data[0].price.id,
        "sender": event.data.object.customer_email,
        "receiver": "Platform",
    }
    serializer = TransactionSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()


class StipeWebhookAPI(APIView):

    def post(self, request):
        event = stripe_webhook(request)
        if(type(event).__name__ == "SignatureVerificationError"):
            return response_exception(event)
        if event.type == 'invoice.payment_succeeded':
            create_subscription_transaction(event)
        if event.type == 'payment_intent.succeeded':
            pass
        return Response()
