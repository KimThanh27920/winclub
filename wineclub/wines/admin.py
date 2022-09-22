from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Wine)
admin.site.register(models.Type)
admin.site.register(models.Food)
admin.site.register(models.Region)
admin.site.register(models.Style)
admin.site.register(models.Grape)
admin.site.register(models.Country)

