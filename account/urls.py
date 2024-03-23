 
 
from .views import *
from django.urls import path

urlpatterns = [
        path('',register,name='register'),
        path('login/',loginUser,name='login'),
        path('logout/',logoutUser,name='logout'),
        

]