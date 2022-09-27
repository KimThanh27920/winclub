import stripe
# Django import
from django.conf import settings

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
