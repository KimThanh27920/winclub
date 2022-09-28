from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("", views.ShippingUnitWineryViewSet, 'shipping_business')
router.register("add-shipping", views.ManageShippingUnitWineryViewSet, 'add_shipping')

urlpatterns = [
    path('', include(router.urls)),
]