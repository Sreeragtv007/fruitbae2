from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page

import random

# Create your views here.


def index(request, **kwargs):

    user = User.objects.all().count()
    category = Category.objects.all()
    products = Product.objects.select_related('categ').all()
    # products=Product.objects.all()
    total_products = products.count()

    p = Paginator(products, 4)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:

        page_obj = p.page(p.num_pages)
    all_products=Product.objects.all()
    
    try:
        random_number = random.randint(0,9) 
        print(random_number)
        herosection=all_products[random_number]
    except:
        herosection=None

    context = {'category': category,
               'user': user, 'total_products': total_products, 'page_obj': page_obj,'herosection':herosection }
    return render(request, 'products.html', context)

@cache_page(60 * 15)
def shopDetails(request, pk):
    product = Product.objects.get(id=pk)
    review = Review.objects.filter(product=pk)

    related_product = Product.objects.filter(categ=product.categ)
    

    context = {'product': product, 'review': review,
               'related_product': related_product}
    return render(request, 'shop-detail.html', context)

@cache_page(60 * 15)
def productFilter(request, pk):
    user = User.objects.all().count()
    category = Category.objects.all()
    products = Product.objects.filter(categ=pk)
    total_products = products.count()

    p = Paginator(products, 4)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:

        page_obj = p.page(p.num_pages)

    context = {'page_obj': page_obj, 'category': category,
               'user': user, 'total_products': total_products}
    return render(request, 'products.html', context)


@login_required(login_url='login')
def addReview(request, pk):
    product = Product.objects.get(id=pk)
    user = request.user
    review = Review.objects.create(
        user=user, product_review=request.POST['review'], product=product)
    review = Review.objects.filter(product=pk)
    return redirect('shopdetails', pk=pk)


def userDetails(request):
    return render(request, 'userdetails.html')


def deleteReview(request, pk):
    review = Review.objects.get(id=pk)

    review.delete()

    return redirect('shopdetails', pk=review.product.id)

# def searchProduct(request):
#     product=Product.objects.filter()


def search(request):
    obj = Product.objects.filter(name__icontains=request.POST.get('search'))
    print(obj)

    context = {'page_obj': obj}
    return render(request, 'products.html', context)
