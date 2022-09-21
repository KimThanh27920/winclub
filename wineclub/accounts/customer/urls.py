<<<<<<< HEAD
from django.urls import path
from . import views


urlpatterns = [
    path('logout/', views.TokenBlacklistView.as_view(), name='logout'),
    path('refresh-token/', views.TokenRefreshView.as_view(), name='refresh_token'),    
    path('profile/', views.ProfileUpdateRetrieveAPIView.as_view(), name='detail-profile'),
    # path('profile/image/', views.UploadImageAPIView.as_view(), name='upload_image'),
    path('profile/change-password/', views.ChangePasswordView.as_view(), name='change_password'),
=======
from django.urls import path, include
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView
from . import views
urlpatterns = [
    path('customer/login/', views.LoginApiView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    # path('register/', views.RegisterApiView.as_view()),
    # path('forgot-password/', views.ForgotPasswordApiView.as_view()),
    # path('reset-password/', views.ChangePasswordWithPINApiView.as_view())
>>>>>>> 5e904269ef05ed4b928ad685f88064f2ab78ff2c
]