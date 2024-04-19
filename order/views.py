from django.shortcuts import render
from cart.models import *
from .models import *



def userOrder(request):
    order=Order.objects.all()
    
    context={'order':order}
    return render(request,'userdetails.html',context)

def cancelOrder(request,pk):
    order=Order.objects.get(id=pk)
    order.delete()
    messages.info(request,"order cancelled sucessfully")
    return redirect('userdetails')
    