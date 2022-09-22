#django import
from django.db import models
from django.contrib.auth import get_user_model

#app import
from coupons.models import Coupon

User = get_user_model()


# Reward Program model class
class RewardProgram(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name="membership_list" )
    require_sending = models.BooleanField(default=False)
    coupons = models.ManyToManyField(Coupon, related_name="coupons_list")
    descriptions= models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="program_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="program_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE, default=None, blank=True, null=True,related_name="program_deleted")

    def __str__(self) -> str:
        return self.name

    
    class Meta:
        db_table = "reward_programs"
