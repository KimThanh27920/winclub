from django.db import models

from wineries.models import Winery
from django.contrib.auth import get_user_model
# Create your models here.

Account = get_user_model()

class Membership(models.Model):
    winery = models.ForeignKey(Winery, on_delete=models.CASCADE, related_name="menbership")

    joined_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField()

    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="membership_created")
    updated_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="membership_updated")
    deleted_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="membership_deleted")

    # def __str__(self):
    #     return self.winery.name