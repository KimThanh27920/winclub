#django import
from django.db import models
from django.contrib.auth import get_user_model

# App import
from categories.models import Style, Type, Grape, Food, Region, Country 
from wineries.models import Winery
from bases.models import BasicLogModel

User = get_user_model()


# Style model class
class Wine(BasicLogModel):
    wine = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    sale = models.FloatField(null=True, blank=True, default=0)
    winery = models.ForeignKey(Winery, on_delete=models.CASCADE, related_name="origin")
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="type_wine")
    style = models.ForeignKey(Style, on_delete=models.CASCADE, related_name="style_wine")
    grape = models.ForeignKey(Grape, on_delete= models.CASCADE, related_name="grape_wine")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="food_pairing")
    region = models.ForeignKey(Region,on_delete=models.CASCADE, related_name="region_wine")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country_wine")
    thumbnail = models.CharField(max_length=255)
    year = models.IntegerField()
    descriptions = models.TextField()
    alcohol = models.FloatField()
    bottle_per_case = models.IntegerField()
    net = models.IntegerField()
    serving_temperature = models.IntegerField()
    in_stock = models.IntegerField()
    
    #taste of wine
    light_bold = models.FloatField()
    smooth_tannic = models.FloatField()
    dry_sweet = models.FloatField()
    soft_acidic = models.FloatField()

    #rating of wine
    average_rating = models.FloatField(default=1)
    reviewers = models.IntegerField
    
    is_active = models.BooleanField(default= False)

    
    class Meta:
        db_table="wines"

    def __str__(self) -> str:
        return self.wine