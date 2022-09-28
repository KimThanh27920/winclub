from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCouponView.as_view(), name='coupon_list'),
    path('<int:coupon_id>/', views.RetrieveCouponView.as_view(), name='coupon_detail'),
]