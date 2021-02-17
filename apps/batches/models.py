from django.db import models

# Create your models here.

class Batches(models.Model):
    name = models.CharField(max_length=100)
    batches = models.PositiveIntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=100)
    message = models.TextField(max_length=50)
    
    
    
  #views
# from rest_framework import generics
# from .models import Contact
# from . serializer import ContactSerializer

# # Create your views here.
# class ContactList(generics.ListCreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer

# class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer


#urls
# from django.urls import path
# from apps.contact import views

# urlpatterns = [
#     path('', views.ContactList.as_view(), name='contact_list'),
#     path('<int:pk>', views.ContactDetail.as_view(), name='contact_detail'),
# ]


#serializers

# from rest_framework import serializers
# from .models import Contact


# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = ['name','batches','date','email','phone']

#models
# from django.db import models
# from phone_field import PhoneField

# # Create your models here.

# class Contact(models.Model):
#     name = models.CharField(max_length=100)
#     batches = models.PositiveIntegerField()
#     date = models.DateField(auto_now=False, auto_now_add=False)
#     email = models.EmailField()
#     phone = PhoneField(blank=True, help_text='Contact phone number')


