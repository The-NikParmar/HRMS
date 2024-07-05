from django.db import models

# Create your models here.
class User(models.Model):
    u_email  = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.u_email
    