from django.db import models
from django.contrib.auth.models import User
from cart.models import *
from django.utils.timezone import now
from django.db.models.fields import CharField

from django.utils.translation import gettext_lazy as _
# Create your models here.
choice = (
    ("WAITING FOR SHIPPING", "waiting for shipping"),
    ("PRODUCT ON THE WAY", "product on the way"),
    ("OUT OF DELIVERY", "out of delivery"),

    ("DELIVERED", "delivered"),
)


class Order(models.Model):
    
    
    choice = (
    ("WAITING FOR SHIPPING", "waiting for shipping"),
    ("PRODUCT ON THE WAY", "product on the way"),
    ("OUT OF DELIVERY", "out of delivery"),

    ("DELIVERED", "delivered"),
)

    product = models.ForeignKey(
        Cart, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    created_date = models.DateTimeField(auto_created=True)
    orderstatus = models.CharField(max_length=50,
                                   choices=choice,
                                   default="WAITING FOR SHIPPING")


class Address(models.Model):
    name = models.TextField()
    address = models.TextField()
    pincode = models.IntegerField()
    email = models.EmailField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    
    
    


