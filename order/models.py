from django.db import models
from django.contrib.auth.models import User
from cart.models import *
# Create your models here.

class Order(models.Model):
    product=models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    address=models.CharField(max_length=200,blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    
    
class Address(models.Model):
     name=models.TextField()
     address=models.TextField()
     pincode=models.IntegerField()
     email=models.EmailField()
     user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    