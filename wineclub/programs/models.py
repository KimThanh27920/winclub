#django import
from django.db import models
from django.contrib.auth import get_user_model

#app import
from coupons.models import Coupon
from bases.models import BasicLogModel

User = get_user_model()


# Reward Program model class
class RewardProgram(BasicLogModel):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name="membership_list" )
    require_sending = models.BooleanField(default=False)
    coupons = models.ManyToManyField(Coupon, related_name="coupons_list")
    descriptions= models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    

    def __str__(self) -> str:
        return self.name

    
    class Meta:
        db_table = "reward_programs"
