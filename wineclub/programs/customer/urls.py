from django.urls import path
from . import views


urlpatterns = [
    # path('', views.ProgramListCreateView.as_view(), name='program_list_create'),
    path('<int:program_id>/', views.RetrieveAPIView.as_view(), name='program_check_condition'),
]