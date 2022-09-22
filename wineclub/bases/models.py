from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Base Model for log
class BasicLogModel(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(default=None, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated')
    deleted_by = models.ForeignKey(User, on_delete= models.CASCADE,default=None, blank=True, null=True, related_name='%(class)s_deleted')


    class Meta:
        abstract=True