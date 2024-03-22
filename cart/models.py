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
    
    def save(self, *args, **kwargs):
        self.total=int(self.qty)*int(self.product.price)
       
        super(Cart, self).save(*args, **kwargs) # Call the real save() method