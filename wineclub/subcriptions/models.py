#django import
from locale import currency
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


#Subcriptions models class
class SubscriptionPackage(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    descriptions = models.TextField()
    currency = models.CharField(max_length=255)
    interval = models.CharField(max_length=255)
    interval_count = models.IntegerField()
    
    is_active = models.CharField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscription_package_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscription_package_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name="subscription_package_deleted")

    class Meta:
        db_table="subscription_package"