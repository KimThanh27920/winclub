#django import
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Type model class
class Type(models.Model):
    type = models.CharField(max_length=255, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="type_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="type_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name="type_deleted")


# Style model class
class Style(models.Model):
    style = models.CharField(max_length=255, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="style_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="style_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name="style_deleted")


# Grape model class
class Grape(models.Model):
    grape = models.CharField(max_length=255, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="grape_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="grape_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name="grape_deleted")


# Food model class
class Food(models.Model):
    food = models.CharField(max_length=255, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="food_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="food_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name="food_deleted")


# Region model class
class Region(models.Model):
    region = models.CharField(max_length=255, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="region_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="region_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name="region_deleted")


# Country model class
class Country(models.Model):
    country = models.CharField(max_length=255, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="country_created")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="country_updated")
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name="country_deleted")