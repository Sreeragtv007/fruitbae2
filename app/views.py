from django.shortcuts import render, redirect
from .models import *

from django.contrib import messages
# Create your views here.


def index(request,**kwargs):
    user=User.objects.all().count()
    category = Category.objects.all()
    products = Product.objects.all()
    total_products=products.count()

    context = {'products': products, 'category': category,'user':user,'total_products':total_products}
    return render(request, 'products.html', context)
        
    

        
 
  


def shop(request, *args, **kwargs):

    context = {}
    return render(request, 'shop.html', context)

def shopDetails(request,pk):
    product=Product.objects.get(id=pk)
    
    context = {'product':product}
    return render(request, 'shop-detail.html', context)

def productFilter(request,pk):
    user=User.objects.all().count()
    category = Category.objects.all()
    products = Product.objects.filter(categ=pk)
    total_products=products.count()

    context = {'products': products, 'category': category,'user':user,'total_products':total_products}
    return render(request, 'products.html', context)
    




