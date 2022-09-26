from django.urls import path
from . import views


urlpatterns = [
    path('', views.CartListCreate.as_view(), name='show_cart'),
]