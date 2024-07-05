from django.shortcuts import render, redirect
from .models import *
import sweetify

# Create your views here.
def home(request):
    return render(request,"home.html")

def register(request):
    if request.POST:
        try:
            User.objects.get(u_email=request.POST['email'])
            sweetify.info(request,"Email is alredy Exists...",timer=2000)
            return redirect('register')
        except:
            if request.POST['pass1']==request.POST['pass2']:
                user = User.objects.create(
                    u_email = request.POST['email'],
                    password = request.POST['pass2']
                )
                print("User created successfully....")
                return render(request,"login.html")
            else:
                print("sorry password conifrm pass can not match")
                return render(request,"register.html")
    else:
        pass
    return render(request,"register.html")

def login(request):
    if request.POST:
        user = User.objects.get(u_email = request.POST['email'])
        if user.password == request.POST['password']:
            request.session['email'] = user.u_email
            sweetify.success(request,"Login Successfully.....")
            return redirect('index')
        else:
            sweetify.error(request,"Criditional Wrong.....")
            return redirect('login')
    else:
        return render(request,"login.html")
    
def forgot_password(request):
    return redirect('forgot_password')