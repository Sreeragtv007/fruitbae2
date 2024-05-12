from django.shortcuts import render,redirect
from cart.models import *
from .models import *
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
import io
import os
from reportlab.pdfgen import canvas
from django.http import HttpResponseBadRequest
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#twst

@login_required(login_url='login')
def userOrder(request):
   
    order = Order.objects.filter(user=request.user)
    

    context = {'order': order}
    invoiceGeneration(request)
    return render(request, 'userdetails.html', context)


def cancelOrder(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    messages.info(request, "order cancelled sucessfully")
    
    return redirect('userdetails')

def onlinePayment(request):
    print('working')
    return redirect('index')

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
def homepage(request,razorpay_total_amount):
    
    currency = 'INR'
    amount = razorpay_total_amount  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'payment.html', context=context)


@csrf_exempt
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


def invoiceGeneration(request):
     print('wooo')
     invoice = Order.objects.filter(
        user=request.user, orderstatus='DELIVERED').filter(invoice_created=False)
     if invoice:
        for i in invoice:
            
            file_path = os.path.join(settings.MEDIA_ROOT, i.product.product.image.path)

            # Create a PDF buffer in memory
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer)
            #p.drawString(30, 800, f'Date{time}')
            p.drawString(100, 750, f'Product name :{i.product.product.name}')
            p.drawImage(file_path, 400, 700, 100, 100)
            p.drawString(100, 700, f'quantity  :{i.product.qty}')
            p.drawString(100, 650, f'total price  :{i.product.total}')
            #p.drawString(100, 600, f'address :{i.address}{i.pincode}')
            p.drawString(100, 550, f'purchase time  :{i.created_date}')

            p.showPage()
            p.save()

        # Retrieve the generated PDF as bytes
            pdf_file = buffer.getvalue()

            # Create a new model instance and save the PDF:
            # my_model = Savepdf.objects.create(name='example1')

            i.file.save(f'generated_pdf{i.id}.pdf', ContentFile(pdf_file))
            i.invoice_created = True
            i.save()
    
            return redirect ('index')
def downloadInvoice(request, pk):
    obj = Order.objects.get(id=pk)
    file_path = os.path.join(settings.MEDIA_ROOT, obj.file.path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404