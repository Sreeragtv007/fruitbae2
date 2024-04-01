from django.shortcuts import render
from cart.models import *
# Create your views here.
def order(request):
    order=Checkout.objects.filter(payment=True)
    if order.count() == 0 :
        messages.info(request,"you have no order")
    context={"order":order}
    return render(request,'userorder.html',context)