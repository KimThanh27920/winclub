#django import
from locale import currency
from operator import mod
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
TYPE_TRANS = [
    ("charge","Charge"),
    ("refund","Refund"),
]


# Transaction model class
class Transaction(models.Model):
    timestamp = models.DateField(auto_now_add=True),
    type = models.CharField(max_length=255,default="charge", choices=TYPE_TRANS)
    amount = models.FloatField()
    currency = models.CharField(max_length=255, default="usd")
    net = models.FloatField()
    fee = models.FloatField()
    unit = models.FloatField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name="money_sender")
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="money_reciever")

    def __str__(self) -> str:
        return self.timestamp
    

    class Meta:
        db_table = "transactions"