from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ListCreateWineAPI.as_view(), name='wine'),
    path('<int:wine_id>/', views.RetrieveUpdateDestroyWineAPI.as_view(), name='rud-wine'),
]