from django.urls import path
from . import views


urlpatterns = [
    path('wineries/', views.ListWineryView.as_view(), name='winery_list'),
    path('wineries/<int:winery_id>/', views.DetailWineryView.as_view(), name='winery'),
]