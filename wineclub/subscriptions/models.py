#django import
from django.db import models
from django.contrib.auth import get_user_model

from bases.models import BasicLogModel

User = get_user_model()


#Subcription Package models class
class SubscriptionPackage(BasicLogModel):
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    descriptions = models.TextField()
    currency = models.CharField(max_length=255)
    interval = models.CharField(max_length=255)
    interval_count = models.IntegerField()
    
    is_active = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.name


    class Meta:
        db_table="subscription_package"