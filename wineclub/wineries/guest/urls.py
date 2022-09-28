from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListWineryView.as_view(), name='winery_list'),
    path('<int:winery_id>/', views.DetailWineryView.as_view(), name='winery'),
]