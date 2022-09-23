from django.db import models
from django.contrib.auth import get_user_model
from bases.models import BasicLogModel
# Create your models here.
Account = get_user_model()

class Notification(BasicLogModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_check = models.BooleanField(default=False)

    def __str__(self):
        return self.title