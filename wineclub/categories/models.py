#django import
from enum import unique
from django.db import models
from django.contrib.auth import get_user_model

# Base import
from bases.models import BasicLogModel
User = get_user_model()


# Type model class
class Type(BasicLogModel):
    type = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    
    def __str__(self):
        return self.type

    
    class Meta:
        db_table="types"
        unique_together = ['type','deleted_at']


# Style model class
class Style(BasicLogModel):
    style = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.style

    
    class Meta:
        db_table="styles"
        unique_together = ['style','deleted_at']

# Grape model class
class Grape(BasicLogModel):
    grape = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.grape

    
    class Meta:
        db_table="grapes"
        unique_together = ['grape','deleted_at']

# Food model class
class Food(BasicLogModel):
    food = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.food

    
    class Meta:
        db_table="foods"
        unique_together = ['food','deleted_at']

# Region model class
class Region(BasicLogModel):
    region = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.region

    
    class Meta:
        db_table="region"
        unique_together = ['region','deleted_at']

# Country model class
class Country(BasicLogModel):
    country = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.country
    
    
    class Meta:
        db_table="countries"
        unique_together = ['country','deleted_at']