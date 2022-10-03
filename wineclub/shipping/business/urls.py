from django.urls import path
from . import views

urlpatterns = [
    path("", views.ShippingUnitWineryAPIView.as_view(), name="list_shipping_unit"),
    path("add-shipping/", views.AddShippingUnitBusinessAPIView.as_view(), name="add_shpping_Unit"),
    path("remove-shipping/", views.RemoveShippingUnitAPIView.as_view(), name="remove_shipping_unit")
]