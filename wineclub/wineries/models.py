from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model

from addresses.models import Address
from bases.models import BasicLogModel

# Create your models here.

Account = get_user_model()

class Winery(BasicLogModel):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name = 'wineries')
    name = models.CharField(max_length=255)
    rating_average = models.FloatField(default=0.0)
    reviewer = models.IntegerField(default=0)
    description = models.TextField()
    postal_code = models.CharField(max_length=255)
    website_url = models.CharField(max_length=255, null=True)
    phone_winery = models.CharField(max_length=255)
    founded_date = models.CharField(max_length=255)
    image_cover = models.ImageField(null=True, upload_to = "images/profile/")
    is_active = models.BooleanField(default=False)
    account_connect = models.CharField(max_length=255, null= True)

    deleted_by = None
    updated_by = None
    created_by = None 

    def __str__(self):
        return self.name