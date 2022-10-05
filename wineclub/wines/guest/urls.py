from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ListWineAPI.as_view(), name='wine'),
    path('<int:wine_id>', views.RetrieveWineAPI.as_view(), name='detail-wine')
]