from django.http import HttpResponseBadRequest
from django.shortcuts import render
from .models import *
from app.models import *

from django.contrib import messages
from django.conf import settings
import razorpay


# Create your views here.
def cart(request, *args, **kwargs):

    cart = Cart.objects.filter(user=request.user).filter(order_complted=False)

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

    if Cart.objects.filter(product=pk).filter(order_complted=False):
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
    cart = Cart.objects.filter(user=request.user).filter(order_complted=False)

    total_price = 0
    for i in cart:
        total_price = total_price + i.product.price
    razorpay_total_amount = total_price * 100
    total=razorpay_total_amount/100

    if request.method == 'GET':

        context = {'cart': cart, 'razorpay_total_amount': razorpay_total_amount,'total':total}
        return render(request, 'checkout.html', context)
    
        
       

        

        

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))



def homepage(request):
     cart = Cart.objects.filter(user=request.user).filter(order_complted=False)
     print(cart)
     total=0
     for i in cart:
         total=total + i.product.price
     
     

     name = request.POST.get('name')
     address = request.POST.get('address')
     pincode = request.POST.get('pincode')
     email = request.POST.get('email')

     checkout = Checkout.objects.create(user=request.user,
                                           name=name,
                                           address=address,
                                           pincode=pincode,
                                           email=email)
        
     for i in cart:
            
        checkout.cart.add(i)
        i.save()
     checkout.total_price=total
     checkout.save()
     
    
    
     currency = 'INR'
     amount = request.POST.get('total_price')  # Rs. 200
 
    # Create a Razorpay Order
     razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
     razorpay_order_id = razorpay_order['id']
     callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
     context = {}
     context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
     context['razorpay_amount'] = amount
     context['currency'] = currency
     context['callback_url'] = callback_url
     context['razorpay_amount_total']=int(amount)/100
     context['razorpay_order_id'] = razorpay_order_id
 
     return render(request, 'payment.html', context=context)





def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
                    
                    
 
                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()