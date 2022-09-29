from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListOrderBusinessAPIView.as_view(), name='list_order'),
    path("<int:order_id>/", views.DetailOrderBusinessAPIView.as_view(), name='detail_order')
]