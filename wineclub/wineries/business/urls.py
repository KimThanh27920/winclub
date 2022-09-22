from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.BusinessProfileView.as_view(), name='business_profile'),
    path('profile/image-cover/', views.UploadImageCover.as_view(), name='upload_image_cover'),
    
]