from .views import *
from django.urls import path

urlpatterns = [
    path('',index,name='index'),
   path('shop/',shop,name='shop'),
   path('shopdetails/<str:pk>/',shopDetails,name='shopdetails'),


]