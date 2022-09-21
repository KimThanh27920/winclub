from django.urls import path, include
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView
from . import views
urlpatterns = [
    path('customer/login/', views.LoginApiView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    # path('register/', views.RegisterApiView.as_view()),
    # path('forgot-password/', views.ForgotPasswordApiView.as_view()),
    # path('reset-password/', views.ChangePasswordWithPINApiView.as_view())
]