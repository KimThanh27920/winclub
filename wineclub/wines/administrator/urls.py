from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ListWineAPI.as_view(), name='wine'),
    path('<int:wine_id>/', views.UpdateWineAPI.as_view(), name='update-wine'),
]