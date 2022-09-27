#django import
from django.db import models
from django.contrib.auth import get_user_model
#App imports
from bases.models import BasicLogModel

User = get_user_model()



TYPE_COUPONS = [
    ("business","business"),
    ("platform","platform")
]

TYPE_REDUCTIONS = [
    ("cash","cash"),
    ("percent","percent")
]
# Coupons model class
class Coupon(BasicLogModel):
    code = models.CharField(max_length=32, unique=True)    
    type = models.CharField(max_length=9, choices=TYPE_COUPONS)
    type_reduce = models.CharField(max_length=9, choices=TYPE_REDUCTIONS)
    coupon_value = models.FloatField()
    max_value = models.FloatField()
    min_order_value = models.FloatField()    
    individual = models.BooleanField(default=True)    
    # amount_off = models.FloatField()
    # percent_off = models.FloatField()
    currency = models.CharField(max_length=10,default="usd")    
    image = models.ImageField(null=True, upload_to = "images/coupons/")
    title = models.CharField(max_length=255)
    description = models.TextField()     
    coupon_amount = models.IntegerField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    def  __str__(self) -> str:
        return self.coupon
    
    class Meta:
        db_table = "coupons"


#Coupons Owner model class
class CouponOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="coupon_owner")
    coupons = models.ManyToManyField(Coupon, related_name="coupons_owner_list")

    def  __str__(self) -> str:
        return self.user
    
    class Meta:
        db_table = "owner_coupons"