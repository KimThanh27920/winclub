#django import
from django.db import models
from django.contrib.auth import get_user_model

#app import
from wineries.models import Winery
from bases.models import BasicLogModel

User = get_user_model()


# Shipping Unit model class
class ShippingUnit(BasicLogModel):
    name = models.CharField(max_length=255, unique=True)
    fee = models.FloatField()
    type = models.CharField(max_length=255)
    expected_date = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


    class Meta:
        db_table = "shipping_unit"


#Shipping service model class
class ShippingBusinessService(BasicLogModel):
    winery = models.ForeignKey(Winery, on_delete= models.CASCADE, related_name="winery_shipping")
    shipping_services= models.ManyToManyField(ShippingUnit, related_name="shipping_service_list")
    
    def __str__(self) -> str:
        return self.winery
    
    
    class Meta:
        db_table ="shipping_business_service"
