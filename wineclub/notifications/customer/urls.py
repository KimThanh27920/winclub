from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ListCreateDeviceAPI.as_view()),
    path('test/', views.TestSendNotifyAPI.as_view())
]