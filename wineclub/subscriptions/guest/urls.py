# Djnango imports
from django.urls import path, include
# App imports
from .views import SubscriptionsPackageGuestViews
#rest framework imports
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", SubscriptionsPackageGuestViews, basename="subscription-packages_admin")

urlpatterns = [
    path("", include(router.urls) ),
]