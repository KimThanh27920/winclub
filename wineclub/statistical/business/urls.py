from django.urls import path
from .views import BusinessStatistical

urlpatterns = [ 
    path('',BusinessStatistical.as_view(), name="business-statistical")
]