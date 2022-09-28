from django.urls import path
from .views import Subscription

urlpatterns =[
    path('subscriptions/',Subscription.as_view(), name="subscription-checkout"),
]
