from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateReviewAPIView.as_view(), name="create_review"),
    path("<int:review_id>/", views.UpdateReviewAPIView.as_view(), name="update_review")
]