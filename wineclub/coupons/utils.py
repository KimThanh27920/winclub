from .models import Coupon


def UpdateAmountCouponUsed(coupon_id):
    try:
        instance = Coupon.objects.get(id=coupon_id)
        if((instance.coupon_amount - 1) > 0 ):
            instance.coupon_amount = instance.coupon_amount - 1
            print(instance.coupon_amount)
        else:
            instance.is_active = False
        
        instance.save()
        return True
    except:
        return False    