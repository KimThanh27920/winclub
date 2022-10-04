from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProgramListView.as_view(), name='program_list'),
    path('<int:program_id>/', views.RetrieveAPIView.as_view(), name='program_retrieve'),
]