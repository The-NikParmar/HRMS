from django.shortcuts import render, redirect, get_object_or_404

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import *
import sweetify
from datetime import datetime
import random
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,"home.html")



def register(request):
    if request.POST:
        try:
            User.objects.get(u_email=request.POST['email'])
            sweetify.info(request,"Email is alredy Exists...")
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
    
def logout(request):
    del request.session['email']
    return redirect('login')
    

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
    emp = Employees.objects.count()
    context={
        'emp':emp
    }
    
    return render(request,"index.html",context)



def employees_list(request):
    employees = Employees.objects.all()
    departments = Department.objects.all()
    designations = Designation.objects.all()
    
    if request.method == "POST":
        if request.POST['password'] == request.POST['cpassword']:
            Employees.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                joining_date=datetime.strptime(request.POST['joining_date'], '%d/%m/%Y').strftime('%Y-%m-%d'),
                employee_id=request.POST['employee_id'],
                phone=request.POST['phone'],
                company=request.POST['company'],
                department=Department.objects.get(id=request.POST['department']),
                designation=Designation.objects.get(id=request.POST['designation']),
            )
            sweetify.success(request, "Employee Add Successfully..")
            return render(request, 'employees_list.html', {'employees': employees, 'departments': departments, 'designations': designations})
        else:
            sweetify.warning(request, "Password and Confirm password do not match")
            return render(request, 'employees_list.html', {'employees': employees, 'departments': departments, 'designations': designations})
    else:
        return render(request, 'employees_list.html', {'employees': employees, 'departments': departments, 'designations': designations})



def employees_search(request):
    employees = Employees.objects.all()
    designations = Designation.objects.all()

    employee_id = request.GET.get('employee_id')
    employee_name = request.GET.get('employee_name')
    designation_id = request.GET.get('designation')

    if employee_id:
        employees = employees.filter(employee_id__icontains=employee_id)
    if employee_name:
        employees = employees.filter(first_name__icontains=employee_name) | employees.filter(last_name__icontains=employee_name)
    if designation_id:
        employees = employees.filter(designation_id=designation_id)

    context = {
        'employees': employees,
        'designations': designations,
    }
    return render(request, 'employees_list.html', context)



def delete_employee(request,id):
    employee=Employees.objects.all()
    print(employee)
    employees = get_object_or_404(Employees, id=id)
    print(employees)
    employees.delete()
    sweetify.success(request,"employee deleted successfully")
    return redirect('employees_list')


def update_employee(request, id):
    employee = get_object_or_404(Employees, pk=id)
    if request.method == 'POST':
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.email = request.POST.get('email')
        department_id = request.POST.get('department')
        designation_id = request.POST.get('designation')
        employee.department = Department.objects.get(id=department_id)
        employee.designation = Designation.objects.get(id=designation_id)
        employee.save()
        sweetify.success(request, "Employee Updated Successfully")
        return redirect('employees_list')
    return render(request, 'employees_list.html')


def departments(request):
    department = Department.objects.all()
    if request.POST:
        dep = Department.objects.create(
            department = request.POST['department']
        )
        sweetify.success(request,"Departments Add Successfully..")
        return render(request,"departments.html",{'department':department})
    else:
        return render(request,"departments.html",{'department':department})
    

def departments_delete(request, id):
    department_instance = get_object_or_404(Department, pk=id)
    department_instance.delete()
    sweetify.success(request, "Department deleted successfully.")
    return redirect('departments')

def update_department(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    if request.method == 'POST':
        department_name = request.POST.get('department')
        department.department = department_name
        department.save()
        sweetify.success(request, "Department updated successfully.")
        return redirect('departments')  
    return render(request, 'departments.html') 


def designations(request):
    designations = Designation.objects.all()
    departments = Department.objects.all()
    
    if request.method == "POST":
        designation = request.POST.get('designation')  
        department_id = request.POST.get('department')  
        
        department = Department.objects.get(id=department_id)
        
        Designation.objects.create(
            designation=designation,
            department=department
        )
        
        sweetify.success(request, "Designation Added Successfully..")
        return redirect('designations')  
    return render(request, "designations.html", {'designations': designations, 'departments': departments})

def designations_update(request, id):
    designations = get_object_or_404(Designation, pk=id)
    if request.method == 'POST':
        designation = request.POST.get('designation')
        department_id = request.POST.get('department')
        department = Department.objects.get(id=department_id)
        
        designations.designation = designation
        designations.department = department
        designations.save()
        
        sweetify.success(request, "Designation updated successfully.")
        return redirect('designations')
    return render(request, 'designations.html')

    
def designations_delete(request, id):
    designation_instance = get_object_or_404(Designation, pk=id)
    designation_instance.delete()
    
    sweetify.success(request, "Designation deleted successfully.")
    return redirect('designations')

def profile(request):
    return render(request,"profile.html")