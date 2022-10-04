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

    
def check_coupon(coupons_arr, instance, instance_price):
    last_coupon = None
    coupon_count = 0
    for coupon in coupons_arr:
        coupons = Coupon.objects.get(id=coupon.get('id'))

        if coupon_count == 1:
            if last_coupon != None and coupons.type != last_coupon.type:
                if coupons.type == "business":
                    if str(coupons.created_by) == str(instance.winery):
                        if int(coupons.coupon_value) > int(instance_price):
                            instance_price = 1
                            coupon_count += 1
                            instance.coupons.add(coupon.get('id'))
                            instance.save()
                            last_coupon = coupons
                        else:
                            instance_price -= coupons.coupon_value
                            coupon_count += 1
                            instance.coupons.add(coupon.get('id'))
                            instance.save()
                            last_coupon = coupons

                if coupons.type == "platform":
                    if int(coupons.coupon_value) > int(instance_price):
                        instance_price = 1
                        coupon_count += 1
                        instance.coupons.add(coupon.get('id'))
                        instance.save()
                        last_coupon = coupons
                    else:
                        instance_price -= coupons.coupon_value
                        coupon_count += 1
                        instance.coupons.add(coupon.get('id'))
                        instance.save()
                        last_coupon = coupons
            else:
                continue

        if coupon_count == 0:
            if coupons.type == "business":
                if str(coupons.created_by) == str(instance.winery):
                    if int(coupons.coupon_value) > int(instance_price):
                        instance_price = 1
                        coupon_count += 1
                        instance.coupons.add(coupon.get('id'))
                        instance.save()
                        last_coupon = coupons
                    else:
                        instance_price -= coupons.coupon_value
                        coupon_count += 1
                        instance.coupons.add(coupon.get('id'))
                        instance.save()
                        last_coupon = coupons

            if coupons.type == "platform":
                if int(coupons.coupon_value) > int(instance_price):
                    instance_price = 1
                    coupon_count += 1
                    instance.coupons.add(coupon.get('id'))
                    instance.save()
                    last_coupon = coupons
                else:
                    instance_price -= coupons.coupon_value
                    coupon_count += 1
                    instance.coupons.add(coupon.get('id'))
                    instance.save()
                    last_coupon = coupons

        if coupon_count >= 2:
            break
    
    return instance_price