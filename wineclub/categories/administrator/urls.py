# django imports
from django.urls import path, include
from .views import TypeAdminAPIView, StyleAdminAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", TypeAdminAPIView, basename="types")

router1 = DefaultRouter()
router1.register("", StyleAdminAPIView, basename="styles")

urlpatterns = [
    path("types/", include(router.urls) ),
     path("styles/", include(router1.urls) ),
]


