from django.urls import path
from . import views


urlpatterns = [
    path('', views.CouponOwnerCreateListView.as_view(), name='coupon_list'),
    path('<int:coupon_id>/', views.CouponRemoveView.as_view(), name='coupon_remove'),
]