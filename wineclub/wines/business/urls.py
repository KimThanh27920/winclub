from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ListCreateWineAPI.as_view(), name='wine'),
]