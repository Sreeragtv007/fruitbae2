from django.shortcuts import render
from .models import *
from app.models import *

from django.contrib import messages


# Create your views here.
def cart(request, *args, **kwargs):
    cart = Cart.objects.filter(user=request.user)
    
    cart_count=cart.count()
    if cart_count == 0:
        messages.info(request,"cart is empty")
    cart_total=0
    for i in cart:
        cart_total=cart_total+i.total
    
    
    
    
    context = {'cart': cart,'cart_count':cart_count,'cart_total':cart_total}
    return render(request, 'cart.html', context)


def addtoCart(request,pk):
    product=Product.objects.get(id=pk)
    cart=Cart.objects.create(product=product,user=request.user)
    cart.save()
    return  redirect('index')


def removeFromCart(request,pk):
    cart=Cart.objects.get(id=pk)
    cart.delete()
    return redirect('cart')

def checkOut(request):
    cart = Cart.objects.filter(user=request.user)
    cart_total=0
    for i in cart:
        cart_total=cart_total+i.total
    context = {'cart': cart,'cart_total':cart_total}
    return render(request,'checkout.html',context)