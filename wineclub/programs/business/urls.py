from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProgramListCreateView.as_view(), name='program_list_create'),
    # path('<int:cart_id>/', views.CartRetrieve.as_view(), name='detail_cart'),
]