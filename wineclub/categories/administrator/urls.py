# django imports
from django.urls import path, include
from .views import (TypeAdminAPIView, StyleAdminAPIView,
                        GrapeAdminAPIView, FoodAdminAPIView,
                         RegionAdminAPIView, CountryAdminAPIView)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", TypeAdminAPIView, basename="types")

router1 = DefaultRouter()
router1.register("", StyleAdminAPIView, basename="styles")

router2 = DefaultRouter()
router2.register("", GrapeAdminAPIView, basename="grapes")

router3 = DefaultRouter()
router3.register("", FoodAdminAPIView, basename="foods")

router4 = DefaultRouter()
router4.register("", RegionAdminAPIView, basename="region")

router5 = DefaultRouter()
router5.register("", CountryAdminAPIView, basename="countries")

urlpatterns = [
    path("types/", include(router.urls) ),
    path("styles/", include(router1.urls) ),
    path("grapes/", include(router2.urls) ),
    path("foods/", include(router3.urls) ),
    path("region/", include(router4.urls) ),
    path("countries/", include(router5.urls) ),
]


