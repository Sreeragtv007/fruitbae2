from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
# Create your views here.

    
def register(request):
    if request.POST:
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if User.objects.filter(username=uname).exists():
            messages.info(request, "user name taken")
            return redirect('register')

        elif pass1 == pass2:
            user = User.objects.create_user(username=uname, password=pass1)
            return redirect('login')
        else:
            messages.info(request, "password does not match")
            return redirect('register')

    return render (request,'register.html')
def loginUser(request):
     if request.POST:
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "user name or password is incorrect")
            return redirect('login')

     return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')