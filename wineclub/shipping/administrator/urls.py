from django.urls import path
from . import views

urlpatterns = [
    path("", views.ShippingUnitAPIView.as_view(), name="list_create_shippingunit"),
    path("<int:shippingunit_id>/", views.UpdateDeleteShippingUnitAPIView.as_view(), name="update_delete_shippingunit")
]