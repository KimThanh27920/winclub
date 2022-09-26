from django.db import models
from django.contrib.auth import get_user_model
from bases.models import BasicLogModel
# Create your models here.

User = get_user_model()

DELIVERY_CHOICES = [
    ("home", "home"),
    ("office", "office")
]

class Address(BasicLogModel):
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    phone = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, default="home", choices=DELIVERY_CHOICES)
    full_name = models.CharField(max_length=255, null=True)
    is_default = models.BooleanField(default=False)
    
    street = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longtitude = models.CharField(max_length=255)
    
    created_by = None
    updated_by = None
    deleted_by = None

