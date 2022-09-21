#django import
from django.db import models
from django.contrib.auth import get_user_model

#app import
from wineries.models import Winery

User = get_user_model()


# Shipping Unit model class
class ShippingUnit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    fee = models.FloatField()
    type = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(default=None, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shipping_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shipping_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,default=None, blank=True, null=True, related_name="shipping_deleted")

    def __str__(self) -> str:
        return self.name


    class Meta:
        db_table = "shipping_unit"


#Shipping service model class
class ShippingBusinessService(models.Model):
    winery = models.ForeignKey(Winery, on_delete= models.CASCADE, related_name="winery_shipping")
    shipping_services= models.ManyToManyField(ShippingUnit, related_name="shipping_service_list")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(default=None, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shipping_service_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shipping_service_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,default=None, blank=True, null=True, related_name="shipping_service_deleted")
    def __str__(self) -> str:
        return self.winery
    
    
    class Meta:
        db_table ="shipping_business_service"
