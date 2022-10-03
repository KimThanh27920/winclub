from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ListCreateBusinessAddressAPI.as_view(), name='cr-address-business'),
    path('<int:address_id>/', views.RetrieveUpdateDestroyBusinessAddressAPI.as_view(), name='rud-address-business')
]