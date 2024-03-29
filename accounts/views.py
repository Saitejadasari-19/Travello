from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/')
    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"User Name already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Id already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request,"User Created")
        else:
            messages.info(request,"Passwod mismatch")
            return redirect('register')
    return render(request,"register.html")
