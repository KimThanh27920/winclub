from django.urls import path
from . import views


urlpatterns = [
    path("", views.OrderAPIView.as_view(), name="create_order"),
    path("<int:order_id>/", views.RetrieveUpdateOrderAPIView.as_view(), name="retrieve_order")
]