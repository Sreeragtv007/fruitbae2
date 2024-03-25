from django.shortcuts import render
from .models import *
from app.models import *

from django.contrib import messages


# Create your views here.
def cart(request, *args, **kwargs):

    cart = Cart.objects.filter(user=request.user)

    cart_count = cart.count()
    if cart_count == 0:
        messages.info(request, "cart is empty")
    cart_total = 0
    for i in cart:
        cart_total = cart_total+i.total

    context = {'cart': cart, 'cart_count': cart_count,
               'cart_total': cart_total}
    return render(request, 'cart.html', context)


def addtoCart(request, pk):

    if Cart.objects.filter(product=pk).exists():
        messages.info(request, "product already added to cart")
        return redirect('index')

    product = Product.objects.get(id=pk)

    cart_obj = Cart.objects.filter(user=request.user)
    cart = Cart.objects.create(product=product, user=request.user)
    cart.save()
    messages.info(request, 'product added to cart sucessfully')
    return redirect('index')


def removeFromCart(request, pk):
    cart = Cart.objects.get(id=pk)
    cart.delete()
    return redirect('cart')


def checkOut(request):
    cart = Cart.objects.filter(user=request.user)

    if request.method == 'GET':


        context = {'cart': cart}
        return render(request, 'checkout.html', context)
    if request.method == "POST":
        qty = request.POST.get("qty")
        
        cart.update(qty=qty)
        
        

        return redirect('checkout')
