# From app
from .models import Winery
from wines.models import Wine



def update_rating_average(wine_id):
    try: 
        instance_wine = Wine.objects.get(id=wine_id)
        obj = Wine.objects.filter(winery=instance_wine.winery.id)
        length = 0
        total_rating = 0
        for wine in obj.values():
            if not (wine['average_rating'] == 0):
                length += 1
                total_rating += wine['average_rating']
        
        average = float(total_rating/length)
        instance_winery = Winery.objects.get(id=instance_wine.winery.id)
        instance_winery.rating_average = average    
        instance_winery.save()
        
        return True
    except:
        return False
    
    