#django import
from django.db import models
from django.contrib.auth import get_user_model

# Base import
from bases.models import BasicLogModel
User = get_user_model()


# Type model class
class Type(BasicLogModel):
    type = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.type

    
    class Meta:
        db_table="types"


# Style model class
class Style(BasicLogModel):
    style = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.style

    
    class Meta:
        db_table="styles"


# Grape model class
class Grape(BasicLogModel):
    grape = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.grape

    
    class Meta:
        db_table="grapes"


# Food model class
class Food(BasicLogModel):
    food = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.food

    
    class Meta:
        db_table="foods"


# Region model class
class Region(BasicLogModel):
    region = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.region

    
    class Meta:
        db_table="region"


# Country model class
class Country(BasicLogModel):
    country = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.country
    
    
    class Meta:
        db_table="countries"