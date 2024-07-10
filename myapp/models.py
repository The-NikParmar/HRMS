from django.db import models


# Create your models here.
class User(models.Model):
    u_email  = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.u_email
    
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department

class Designation(models.Model):
    designation = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.designation

class Employees(models.Model):
    

    COMPANY_CHOICES = [
        ("Delta", "Delta"),
        ("infotech", "infotech"),
        ("TCS", "TCS"),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    joining_date = models.DateField(blank=True, null=True)
    employee_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    company = models.CharField(max_length=20, choices=COMPANY_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class Holidays(models.Model):
    
    holiday_name = models.CharField(max_length=50)
    holiday_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.holiday_name
    




    
