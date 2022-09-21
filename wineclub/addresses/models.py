from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

DELIVERY_CHOICES = [
    ("home", "home"),
    ("office", "office"),
]

class Address(models.Model):
    street = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longtitude = models.CharField(max_length=255)


class Delivery(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default="home", choices=DELIVERY_CHOICES)
    full_name = models.CharField(max_length=255)
    is_default = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    