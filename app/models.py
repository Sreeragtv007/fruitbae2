from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(
        upload_to='images', default='image not available')

    thumbnails = models.ImageField(upload_to='thumbnail', blank=True)

    categ = models.ForeignKey(
        'category', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    product_review=models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True, null=True)
    

