from django.db import models

# Create your models here.

class SignupDB(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Repeate=models.CharField(max_length=100,null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Gender=models.CharField(max_length=100,null=True,blank=True)

class ContactDB(models.Model):
    CONTACT_NAME=models.CharField(max_length=100,null=True,blank=True)
    CONTACT_EMAIL=models.EmailField(null=True,blank=True)
    CONTACT_SUBJECTS=models.CharField(max_length=100,null=True,blank=True)
    CONTACT_MESSAGE=models.TextField(max_length=100,null=True,blank=True)

