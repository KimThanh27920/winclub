from django.urls import path
from .views import Subscription

urlpatterns =[
    path('checkout/',Subscription.as_view(), name="subscription-checkout"),
]
