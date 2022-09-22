from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
urlpatterns = [

    path('login/', views.LoginApiView.as_view(), name='login'),
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('business/register/', views.BusinessRegisterAPI.as_view(), name='business-register'),
    path('forgot-password/', views.ForgotPasswordApiView.as_view()),
    path('forgot-password/confirm/', views.ChangePasswordWithPINApiView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view())
]