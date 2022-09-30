from django.db import models

from wineries.models import Winery
from django.contrib.auth import get_user_model
# Create your models here.

Account = get_user_model()

class Membership(models.Model):
    winery = models.OneToOneField(Winery, on_delete=models.CASCADE, related_name="membership")
    users = models.ManyToManyField(Account, related_name="membership_user")

    def __str__(self):
        return self.winery