from pyexpat import model
from django.db import models

from wineries.models import Winery
from django.contrib.auth import get_user_model
from bases.models import BasicLogModel
# Create your models here.

Account = get_user_model()

class Membership(models.Model):
    winery = models.ForeignKey(Winery, on_delete=models.CASCADE, related_name="membership")
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="membership_user")

    # def __str__(self):
    #     return self.winery.name