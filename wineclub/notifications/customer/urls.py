from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ListNotificationAPI.as_view()),
    path('<int:notification_id>/', views.UpdateNotificationAPI.as_view()),
    path('device/', views.ListCreateDeviceAPI.as_view()),
    path('test/', views.TestSendNotifyAPI.as_view())
]