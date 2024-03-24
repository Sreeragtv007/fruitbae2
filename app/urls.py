from .views import *
from django.urls import path

urlpatterns = [
   path('',index,name='index'),
   path('shop/',shop,name='shop'),
   path('shopdetails/<str:pk>/',shopDetails,name='shopdetails'),
   path('filter/<str:pk>/',productFilter,name='productfilter'),
   path('addreview/<str:pk>/',addReview,name='addreview'),


]