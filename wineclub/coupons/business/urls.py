from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateListCounponView.as_view(), name='coupon_create_list'),
    path('<int:coupon_id>/', views.RetrieveUpdateDestroyCouponView.as_view(), name='coupon_update_destroy'),
]