#django import
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
TYPE_TRANS = [
    ("charge","Charge"),
    ("refund","Refund"),
]


# Transaction model class
class Transaction(models.Model):

    timestamp = models.CharField(max_length=20)
    type = models.CharField(max_length=255,default="charge", choices=TYPE_TRANS)
    amount = models.BigIntegerField()
    currency = models.CharField(max_length=255, default="usd")
    net = models.BigIntegerField()
    fee = models.BigIntegerField()
    unit = models.IntegerField(default=100)
    description = models.TextField(null=True)
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.timestamp
    

    class Meta:
        db_table = "transactions"