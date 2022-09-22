from django.db import models
from django.contrib.auth import get_user_model

from addresses.models import Address

# Create your models here.

Account = get_user_model()

class Winery(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
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

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField()

    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="winery_created")
    updated_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="winery_updated")
    deleted_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="winery_deleted")

    def __str__(self):
        return self.name