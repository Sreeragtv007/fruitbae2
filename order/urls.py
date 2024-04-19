from .views import *
from django.urls import path

urlpatterns = [
        
        path('userdetails/',userOrder,name='userdetails'),
        path('cancelorder/<str:pk>/',cancelOrder,name='cancelorder'),
        
]
       

