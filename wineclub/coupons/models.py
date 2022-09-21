#django import
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Coupons model class
class Coupon(models.Model):
    code = models.CharField(max_length=32, unique=True)
    coupon = models.CharField(max_length=255)
    type = models.CharField(max_length=8)
    is_refund_coin = models.BooleanField(default=False)
    amount_off = models.FloatField()
    currency = models.CharField(max_length=255)
    percent_off = models.FloatField()
    image = models.CharField(max_length=255)
    descriptions = models.TextField()
    times = models.IntegerField()
    min_order_value = models.FloatField()
    max_value = models.FloatField()
    used = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(default=None, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="coupon_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="coupon_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,default=None, blank=True, null=True, related_name="coupon_deleted")

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