from django.db import models

# Create your models here.
class Records(models.Model):
    created_at=models.DateTimeField(auto_now_add=True) 
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=120) 
    email=models.EmailField(max_length=250)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=250)
    city= models.CharField(max_length=60)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=25)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")