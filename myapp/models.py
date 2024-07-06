from django.db import models

# Create your models here.
class User(models.Model):
    u_email  = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.u_email
    
class Employees(models.Model):
    company=(
        ("Delta","Delta"),
        ("infotech","infotech"),
        ("TCS","TCS"),
        
    )

    department=(
        ("Web Development","Web Development"),
        ("Marketing","Marketing"),
        ("Backend Development","Backend Development"),
        ("Frontend Development","Frontend Development"),
    )

    designation=(
        ("Web Designer","Web Designer"),
        ("Web Developer","Web Developer"),
        ("Android Developer","Android Developer"),
        ("Backend Developer","Backend Developer")
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    joining_date = models.DateField(blank=True, null=True)
    employee_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    company = models.CharField(max_length=20,choices=company)
    department = models.CharField(max_length=20,choices=department)
    designation = models.CharField(max_length=20,choices=designation)

    def __str__(self):
        return self.first_name
    
