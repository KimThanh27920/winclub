from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
Account = get_user_model()

class Notification(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_check = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)
    deleted_at = models.DateField()

    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="notifycation_created")
    deleted_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="notifycation_deleted")

    def __str__(self):
        return self.title