from django.urls import path, include
from .views import TransactionAdminView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", TransactionAdminView, basename="transactions-admin")

urlpatterns = [
    path("", include(router.urls) ),
]