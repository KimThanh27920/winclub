from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListReviewsAPIView.as_view(), name="list_all_review")
]