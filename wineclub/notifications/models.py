from enum import auto
from django.db import models
from django.contrib.auth import get_user_model
from bases.models import BasicLogModel
# Create your models here.
Account = get_user_model()

class Notification(models.Model):
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_check = models.BooleanField(default=False)

    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
