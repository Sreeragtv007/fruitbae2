 
 
from .views import *
from django.urls import path

urlpatterns = [
        path('',cart,name='cart'),
        path('addtocart/<str:pk>/',addtoCart,name='addtocart'),
        path('remove-from-cart/<str:pk>/',removeFromCart,name='remove-from-cart'),
        path('checkout/',checkOut,name='checkout'),
         path('payment/',homepage, name='payment'),
         path('paymenthandler/',paymenthandler, name='paymenthandler'),
        


]