import stripe
#rest framework 
from rest_framework.response import Response
from rest_framework import status
# Django import
from django.conf import settings
from datetime import datetime

stripe.api_key=settings.STRIPE_SECRET_KEY


class StripeAPI:

    # create price subscription package 
    def create_price(name, price, currency, interval,interval_count):
        product_id = stripe.Product.create(name=name)
        price_id = stripe.Price.create(
            unit_amount= price, 
            currency=currency,
            recurring={
                "interval": interval,
                "interval_count": interval_count
                },
            product=product_id,
            )
        return price_id.id

    # checkout subscription
    def subscription_checkout(stripe_account, price_id):
        try:
            subscription = stripe.Subscription.create(
                customer = stripe_account,
                items=[
                    {"price": price_id },
                ],
            )

            data = {
                "id": subscription["id"],
                "created": datetime.fromtimestamp(subscription["created"]),
                "unit_amount": subscription["items"]["data"][0]["price"]["unit_amount"],
                "currency":subscription["currency"],
                "interval": subscription["items"]["data"][0]["price"]["recurring"]["interval"],
                "interval_amount": subscription["items"]["data"][0]["price"]["recurring"]["interval_count"],
                "next_payment_date": datetime.fromtimestamp(subscription["current_period_end"]),
                "status": subscription["status"]
            }
        except stripe.error.InvalidRequestError:
            data = {"status": "Failed"}
            return data
        return data
        