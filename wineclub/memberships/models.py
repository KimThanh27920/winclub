from django.db import models

from wineries.models import Winery
from django.contrib.auth import get_user_model
from bases.models import BasicLogModel
# Create your models here.

Account = get_user_model()

class Membership(BasicLogModel):
    winery = models.ForeignKey(Winery, on_delete=models.CASCADE, related_name="menbership")

    joined_at = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.winery.name