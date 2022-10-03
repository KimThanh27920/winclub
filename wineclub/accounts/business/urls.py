from django.urls import path
from . import views


urlpatterns = [
    path('', views.StripeConnectRegistration.as_view()),
    path('account/', views.RetrieveConnectAPI.as_view())
]