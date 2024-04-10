from .views import *
from django.urls import path

urlpatterns = [
   path('',index,name='index'),
   path('shopdetails/<str:pk>/',shopDetails,name='shopdetails'),
   path('filter/<str:pk>/',productFilter,name='productfilter'),
   path('addreview/<str:pk>/',addReview,name='addreview'),
   path('userdetails/',userDetails,name='userdetails'),


]