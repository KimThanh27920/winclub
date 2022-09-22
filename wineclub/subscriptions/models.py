#django import
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


#Subcription Package models class
class SubscriptionPackage(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    descriptions = models.TextField()
    currency = models.CharField(max_length=255)
    interval = models.CharField(max_length=255)
    interval_count = models.IntegerField()
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True,)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscription_package_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscription_package_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,default=None, blank=True, null=True, related_name="subscription_package_deleted")

    def __str__(self) -> str:
        return self.name


    class Meta:
        db_table="subscription_package"