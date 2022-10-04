from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProgramListCreateView.as_view(), name='program_list_create'),
    path('<int:program_id>/', views.RemoveUpdateAPIView.as_view(), name='program_update_remove'),
]