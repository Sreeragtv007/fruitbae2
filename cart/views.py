from django.shortcuts import render
from .models import *
from app.models import *


# Create your views here.
def cart(request, *args, **kwargs):
    cart = Cart.objects.filter(user=request.user)

    context = {'cart': cart}
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