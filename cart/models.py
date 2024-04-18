from django.db import models

from django.contrib.auth.models import User
from app.views import *

# Create your models here.
class Cart(models.Model):

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    qty = models.IntegerField(default=1)
    total = models.IntegerField(blank=True, null=True)
    order_complted=models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.total=int(self.qty)*int(self.product.price)
       
        super(Cart, self).save(*args, **kwargs) # Call the real save() method
        

    
class Checkout(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    name=models.CharField(max_length=50,blank=True, null=True)
    address=models.CharField(max_length=50,blank=True, null=True)
    pincode=models.IntegerField(blank=True, null=True)
    email=models.CharField(max_length=50,blank=True, null=True)
    total_price=models.IntegerField(blank=True, null=True) 
    payment=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now=True)

    
 
    