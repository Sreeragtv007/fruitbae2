from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


@login_required(login_url='login')
def index(request, **kwargs):
    
    user = User.objects.all().count()
    category = Category.objects.all()
    products = Product.objects.all()
    total_products = products.count()

    p = Paginator(products,2)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        
        page_obj = p.page(p.num_pages)


    context = { 'category': category,
               'user': user, 'total_products': total_products,'page_obj': page_obj, }
    return render(request, 'products.html', context)


@login_required(login_url='login')
def shop(request, *args, **kwargs):
    category=Category.objects.all()
    products=Product.objects.all()
                

    context = {'category':category,'products':products}
    return render(request, 'shop.html', context)


@login_required(login_url='login')
def shopDetails(request, pk):
    product = Product.objects.get(id=pk)

    context = {'product': product}
    return render(request, 'shop-detail.html', context)


@login_required(login_url='login')
def productFilter(request, pk):
    user = User.objects.all().count()
    category = Category.objects.all()
    products = Product.objects.filter(categ=pk)
    total_products = products.count()

    context = {'products': products, 'category': category,
               'user': user, 'total_products': total_products}
    return render(request, 'products.html', context)
