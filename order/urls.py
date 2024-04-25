from .views import *
from django.urls import path

urlpatterns = [
        
        path('userdetails/',userOrder,name='userdetails'),
        path('cancelorder/<str:pk>/',cancelOrder,name='cancelorder'),
        path('payment/',onlinePayment,name='payment'),
         path('homepage/',homepage, name='index'),
        path('paymenthandler/',paymenthandler, name='paymenthandler'),
]
       

