#django import
from hashlib import md5
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model

#app import
from addresses.models import Delivery
from shipping.models import ShippingUnit
from wines.models import Wine
from wineries.models import Winery
from coupons.models import Coupon
from bases.models import BasicLogModel

User = get_user_model()
STATUS_CHOICES = [
    ("processing", "Processing"),
    ("shipping", "Shipping"),
    ("completed", "Completed"),
    ("canceled", "Canceled"),

]
PAYMENT_CHOICES = [
    ("charged","charged"),
    ("refund","refunded"),
    (None, None)
]
# Order model class
class Order(BasicLogModel):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer")
    winery = models.ForeignKey(Winery, on_delete=models.CASCADE, related_name="winery")
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name="delivery_address")
    shipping_service = models.ForeignKey(ShippingUnit, on_delete=models.CASCADE, related_name="shipping_service")
    coupons = models.ManyToManyField(Coupon, related_name="coupons_apply")
    note = models.TextField(null=True, blank=True)
    used_points = models.FloatField()
    total = models.FloatField(default=0)
    status = models.CharField(max_length= 255, default="processing", choices=STATUS_CHOICES)
    payment = models.CharField(default=None,max_length=255,choices=PAYMENT_CHOICES)
    

    def __str__(self) -> str:
        return self.id
    

    class Meta:
        db_table = "orders"


#Order detail models class
class OrderDetail(models.Model):
    quatity = models.IntegerField()
    price = models.FloatField()
    sale = models.FloatField(null=True, blank = True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_id")
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name="wine_order")

    def __str__(self) -> str:
        return self.wine
    

    class Meta:
        db_table = "order_detail"

