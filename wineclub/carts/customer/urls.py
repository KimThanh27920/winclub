from django.urls import path
from . import views


urlpatterns = [
    path('', views.CartListCreate.as_view(), name='show_cart'),
    path('<int:cart_id>/', views.CartRetrieve.as_view(), name='detail_cart'),
]