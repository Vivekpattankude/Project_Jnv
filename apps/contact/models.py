from django.db import models
from phone_field import PhoneField

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    batches = models.PositiveIntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    phone = models.CharField(max_length=12)
    message = models.TextField(max_length=25)
    

