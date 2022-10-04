# From app
from .models import Winery
from wines.models import Wine



def update_rating_average(wine_id):
    try: 
        instance_wine = Wine.objects.get(id=wine_id)
        print(instance_wine)
        obj = Wine.objects.filter(winery=instance_wine.winery.id)
        length = len(obj)
        print(length)
        total_rating = 0
        for wine in obj.values():
            total_rating += wine['average_rating']
        
        average = float(total_rating/length)
        print(average)
        instance_winery = Winery.objects.get(id=instance_wine.winery.id)
        instance_winery.average_rating = average    
        instance_winery.save()
        return True
    
    except:
        return False
    
    