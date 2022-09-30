from django.urls import path
from .views import AdminStatistical

urlpatterns = [ 
    path('',AdminStatistical.as_view(), name="admin-statistical")
]