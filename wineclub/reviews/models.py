#django import
from django.db import models
from django.contrib.auth import get_user_model

#app import
from wines.models import Wine

User = get_user_model()


# Review model class
class Review(models.Model):
    content = models.CharField(max_length=255)
    rating = models.IntegerField()
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name="wine_rating")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rating")
    created_at = models.DateTimeField()
    # admin can be deleted
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rating_deleted") 

    def __str__(self) -> str:
        return self.rating
    

    class Meta:
        db_table = "reviews"