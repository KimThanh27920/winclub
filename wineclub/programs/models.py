#django import
from stat import UF_OPAQUE
from django.db import models
from django.contrib.auth import get_user_model

#app import
from coupons.models import Coupon
from wines.models import Wine
from bases.models import BasicLogModel

User = get_user_model()


# Reward Program model class
class RewardProgram(BasicLogModel):
    name = models.CharField(max_length=255)    
    require_sending = models.BooleanField(default=False)    
    total_price_require = models.IntegerField(default=0)
    coupons = models.ManyToManyField(Coupon, related_name="coupons_list")
    wines = models.ManyToManyField(Wine, related_name="wine_list", blank=True)
    members = models.ManyToManyField(User, related_name="membership_list", blank=True)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    
    created_by = None
    updated_by = None
    deleted_by= None

    def __str__(self) -> str:
        return self.name

    
    class Meta:
        db_table = "reward_programs"
