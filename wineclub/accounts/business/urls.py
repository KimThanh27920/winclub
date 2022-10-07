from django.urls import path
from . import views


urlpatterns = [
    # path('', views.StripeConnectRegistration.as_view()),
    path('', views.RegisterConnectAccountAPI.as_view()),
    path('account/', views.RetrieveConnectAPI.as_view()),
    # path('account/stripe-connect/', views.RegisterConnectAccountAPI.as_view()),
]