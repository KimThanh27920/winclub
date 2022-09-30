from django.urls import path
from . import views


urlpatterns = [
    path('', views.MembershipCreateListView.as_view(), name='member_list'),
    path('<str:email>/', views.MembershipRemoveView.as_view(), name='member_remove'),
]