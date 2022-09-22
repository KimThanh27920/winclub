from django.urls import path, include
from .views import (TypeAPIView, StyleAPIView,
                        GrapeAPIView, FoodAPIView,
                         RegionAPIView, CountryAPIView)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", TypeAPIView, basename="types_guest")

router1 = DefaultRouter()
router1.register("", StyleAPIView, basename="styles_guest")

router2 = DefaultRouter()
router2.register("", GrapeAPIView, basename="grapes_guest")

router3 = DefaultRouter()
router3.register("", FoodAPIView, basename="foods_guest")

router4 = DefaultRouter()
router4.register("", RegionAPIView, basename="region_guest")

router5 = DefaultRouter()
router5.register("", CountryAPIView, basename="countries_guest")

urlpatterns = [
    path("types/", include(router.urls) ),
    path("styles/", include(router1.urls) ),
    path("grapes/", include(router2.urls) ),
    path("foods/", include(router3.urls) ),
    path("region/", include(router4.urls) ),
    path("countries/", include(router5.urls) ),
]
