from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCounponView.as_view(), name='coupon_list'),
    path('<int:coupon_id>/', views.UpdateCouponView.as_view(), name='coupon_update_active'),
]