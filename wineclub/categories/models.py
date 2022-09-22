#django import
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Type model class
class Type(models.Model):
    type = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="type_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="type_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE, default=None, blank=True, null=True,related_name="type_deleted")
    
    def __str__(self):
        return self.type

    
    class Meta:
        db_table="types"


# Style model class
class Style(models.Model):
    style = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="style_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="style_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,default=None, blank=True, null=True, related_name="style_deleted")

    def __str__(self) -> str:
        return self.style

    
    class Meta:
        db_table="styles"


# Grape model class
class Grape(models.Model):
    grape = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(default=None, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="grape_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="grape_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,default=None, blank=True, null=True, related_name="grape_deleted")

    def __str__(self) -> str:
        return self.grape

    
    class Meta:
        db_table="grapes"


# Food model class
class Food(models.Model):
    food = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(default=None, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="food_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="food_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,default=None, blank=True, null=True,related_name="food_deleted")

    def __str__(self) -> str:
        return self.food

    
    class Meta:
        db_table="foods"


# Region model class
class Region(models.Model):
    region = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(default=None, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="region_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="region_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,default=None, blank=True, null=True,related_name="region_deleted")

    def __str__(self) -> str:
        return self.region

    
    class Meta:
        db_table="region"


# Country model class
class Country(models.Model):
    country = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(default=None, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="country_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="country_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,default=None, blank=True, null=True,related_name="country_deleted")

    def __str__(self) -> str:
        return self.country
    
    
    class Meta:
        db_table="countries"