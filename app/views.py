from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def index(request, *args, **kwargs):

    products = Product.objects.all()
    category = Category.objects.all()

    context = {'products': products, 'category': category}
    return render(request, 'products.html', context)


def shop(request, *args, **kwargs):

    context = {}
    return render(request, 'shop.html', context)


