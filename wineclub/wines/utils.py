from .models import Wine


def UpdateAmountCouponUsed(wine_id, amount_order):
        instance = Wine.objects.get(id=wine_id)
        instance.in_stock = instance.in_stock - amount_order
        instance.save()