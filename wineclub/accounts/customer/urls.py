from django.urls import path
from . import views


urlpatterns = [
    path('logout/', views.TokenBlacklistView.as_view(), name='logout'),
    path('refresh-token/', views.TokenRefreshView.as_view(), name='refresh_token'),    
    path('profile/', views.ProfileUpdateRetrieveAPIView.as_view(), name='detail-profile'),
    # path('profile/image/', views.UploadImageAPIView.as_view(), name='upload_image'),
    path('profile/change-password/', views.ChangePasswordView.as_view(), name='change_password'),
]