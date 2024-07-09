"""
URL configuration for HRMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('index', views.index, name='index'),
    path('otp', views.otp, name='otp'),
    path('reset_password', views.reset_password, name='reset_password'),

    path('employee_dashboard', views.employee_dashboard, name='employee_dashboard'),
    path('employees_list', views.employees_list, name='employees_list'),
    path('employees_search', views.employees_search, name='employees_search'),
    path('delete_employee/ <int:id>/', views.delete_employee, name='delete_employee'),
    path('update_employee/<int:id>', views.update_employee, name='update_employee'),
    path('profile', views.profile, name='profile'),



    path('departments', views.departments, name='departments'),
    path('departments_delete/<int:id>', views.departments_delete, name='delete_department'),  # Added this line
    path('departments/<int:department_id>/update/', views.update_department, name='update_department'),


    path('designations', views.designations, name='designations'),
    path('designations_update/<int:id>', views.designations_update, name='designations_update'),
    path('designations_delete/<int:id>', views.designations_delete, name='designations_delete'),  # Add this line



]
