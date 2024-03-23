 
 
from .views import *
from django.urls import path

urlpatterns = [
        path('',register,name='register'),
        path('login',login_user,name='login'),
        path('logout',login_user,name='logout'),
        

]