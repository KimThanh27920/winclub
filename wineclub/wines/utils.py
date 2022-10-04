from .models import Wine


def decrease_in_stock_wine(wine_id, amount_order):
        instance = Wine.objects.get(id=wine_id)
        instance.in_stock = instance.in_stock - amount_order
        instance.save()