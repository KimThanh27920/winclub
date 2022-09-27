from django.urls import path, include
from . import views

urlpatterns = [
    path("payment-methods/", views.PaymentMethodAPIView.as_view(), name='add_payemnt_methods'),
    path("payment-methods/<str:pm_id>/", views.DeletePaymentMethodAPIView.as_view(), name='delete_payemnt_methods'),
]