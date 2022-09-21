from django.db import models
from django.contrib.auth import get_user_model

from addresses.models import Address

# Create your models here.

Account = get_user_model()

class Winery(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="winery")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="winery")
    name = models.CharField(max_length=255)
    rating_average = models.FloatField(default=0.0)
    reviewer = models.IntegerField(default=0)
    description = models.TextField()
    postal_code = models.CharField(max_length=255)
    website_url = models.CharField(max_length=255, null=True)
    phone_winery = models.CharField(max_length=255)
    founded_date = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)


class Membership(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="membership_account")
    winery = models.ForeignKey(Winery, on_delete=models.CASCADE, related_name="membership_winery")
