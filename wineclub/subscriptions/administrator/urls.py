# django imports
from django.urls import path, include
from .views import SubscriptionsPackageAdminAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", SubscriptionsPackageAdminAPIView, basename="subscription-packages_admin")

urlpatterns = [
    path("", include(router.urls) ),
]