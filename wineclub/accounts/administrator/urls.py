# django imports
from django.urls import path, include
from .views import (ManageCustomer, ManageBusiness)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", ManageCustomer, basename="manage-customer")

router1 = DefaultRouter()
router1.register("", ManageBusiness, basename="manage-business")

urlpatterns = [
    path("customers/", include(router.urls) ),
    path("businesses/", include(router1.urls) ),
]


