from django.db import models
from django.contrib.auth.models import User
from cart.models import *
# Create your models here.
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    