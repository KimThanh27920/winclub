#django import
from django.db import models
from django.contrib.auth import get_user_model
from bases.models import BasicLogModel
#app import
from wines.models import Wine

User = get_user_model()


# Review model class
class Review(BasicLogModel):
    content = models.TextField()
    rating = models.IntegerField(default=0)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name="wine_rating")
    reply = models.ForeignKey("self", null=True, on_delete=models.CASCADE, blank=True)
    

    def __str__(self) -> str:
        return self.rating
    

    class Meta:
        db_table = "reviews"