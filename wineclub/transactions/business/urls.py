from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.ListTransactionAPI.as_view()),
]