from django.shortcuts import render
from cart.models import *
# Create your views here.
# def order(request):
#     order=Checkout.objects.filter(payment=True)
#     if order.count() == 0 :
#         messages.info(request,"you have no order")
#     context={"order":order}
#     return render(request,'userorder.html',context)

# from django.utils import timezone
# def order(request):
#     # Start measuring time
#     start_time = timezone.now()

#     products = Product.objects.all()

#     # Calculate time taken
#     end_time = timezone.now()
#     elapsed_time = end_time - start_time
#     response['X-Elapsed-Time'] = elapsed_time.total_seconds()

#     return response