from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

def validateCin(value):
    if len(value) !=8:
        raise ValidationError("Cin must has 8 characters")
    
    
    
class Person(AbstractUser):
    cin = models.CharField(primary_key=True,max_length=8, validators=[validateCin])
    email = models.EmailField("Email",max_length=20)
    username = models.CharField(max_length=20,unique=True)
    
    #hedha besh naffichi fel partie admin par email
    def __str__(self):
        return self.username
    
    #hedha besh nbadal esm l models men users l persons
    class Meta:
        verbose_name = 'Person'
