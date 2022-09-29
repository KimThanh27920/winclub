from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListOrderAdminAPIView.as_view(), name='list_order_admin'),
    path("<int:order_id>/", views.RetrieveOrderAdminAPIView.as_view(), name='retrieve_order_admin')
]