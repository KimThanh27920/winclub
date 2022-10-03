# From django
from django.db import models
from django.contrib.auth import get_user_model
# From app
from coupons.models import Coupon
from bases.models import BasicLogModel

User = get_user_model()



# Reward Program model class
class RewardProgram(BasicLogModel):
    name = models.CharField(max_length=255, unique=True)       
    total_price_require = models.IntegerField(default=0)
    coupons = models.ManyToManyField(Coupon, related_name="coupons_list")
    description = models.TextField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "reward_programs"
