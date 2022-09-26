from django.urls import path
from .views import (CategoriesAPIView)

urlpatterns = [
    path('', CategoriesAPIView.as_view(), name="categories-guest-view"),
]
