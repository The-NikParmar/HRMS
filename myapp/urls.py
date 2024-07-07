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
    path('employees_list', views.employees_list, name='employees_list'),
    path('employees_serch', views.employees_serch, name='employees_serch'),
    path('delete_employee/ <int:id>/', views.delete_employee, name='delete_employee'),

    path('departments', views.departments, name='departments'),


]
