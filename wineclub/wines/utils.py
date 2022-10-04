from .models import Wine
from wineries.utils import update_rating_average

def decrease_in_stock_wine(wine_id, amount_order):
    instance = Wine.objects.get(id=wine_id)
    instance.in_stock = instance.in_stock - amount_order
    instance.save()


def update_reviews(wine_id, rating):
    instance = Wine.objects.get(id=wine_id)
    if(instance.reviewers):
        total_rating = (instance.average_rating * instance.reviewers) + rating
        instance.reviewers +=1
        instance.average_rating = total_rating / instance.reviewers
        print(instance.reviewers)
    else:
        instance.average_rating = rating
        instance.reviewers +=1
    instance.save()
    update_rating_average(wine_id)
