from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import *
import sweetify
import random

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
    

def mymailfunction(subject,template,to,context):
    template_str = template+'.html'
    html_message = render_to_string(template_str, {'data': context})
    plain_message = strip_tags(html_message)
    from_email = 'nikhilparmar1015@gmail.com'
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        
    
def forgot_password(request):
    if request.method == 'POST':
        
        try:
            user = User.objects.get(u_email=request.POST['email'])
            email = request.POST['email']
            otp = random.randint(1001, 9999)
            request.session['email'] = email
            request.session['otp'] = otp

            # Assuming mymailfunction is a custom function for sending emails
            mymailfunction("Welcome to Forget Password", "etemplate", email, {'email': email, "otp": otp})

            return render(request, "otp.html")
        except User.DoesNotExist:
            sweetify.warning(request, "Email does not exist!")
            return render(request, "forgot_password.html")
    else:
        return render(request, "forgot_password.html")
    
    
def otp(request):
    if request.POST:
        otp=int(request.session['otp'])
        uotp=int(request.POST['uotp'])
        print(otp)
        print(uotp)
        if otp==uotp:
            del request.session['otp']
            return render(request,"reset_password.html")
        else:
            msg="Invalid OTP"
            sweetify.error(request,msg)
            return render(request,"otp.html")
    else:
        return render(request,"otp.html")
    
def reset_password(request):   
    if request.POST:
            user= User.objects.get(u_email=request.session['email'])
            if request.POST['npassword']==request.POST['ncpassword']:
                user.password=request.POST['ncpassword']
                user.save()
                msg="Password Reset successfuly..." 
                sweetify.success(request,msg)
                del request.session['email']
                return render(request,"login.html")
               
            else:
                msg="New Password and Confirm New Password Does Not Match" 
                sweetify.error(request,msg)
                return render(request,"reset_password.html")
    else:
          return render(request,"reset_password.html")

def index(request):
    return render(request,"index.html")


