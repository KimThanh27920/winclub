from django.urls import path
from .views import Subscription, SubscriptionCancel

urlpatterns =[
    path('subscriptions/',Subscription.as_view(), name="subscription-checkout"),
    path('cancel/',SubscriptionCancel.as_view(), name="subscription-canceled"),
]
