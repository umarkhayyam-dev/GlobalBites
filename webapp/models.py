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


# class cartDB(models.Model):
#     Username=models.CharField(max_length=100,null=True,blank=True)
#     Book_name=models.CharField(max_length=100,null=True,blank=True)
#     Quantity=models.IntegerField(null=True,blank=True)
#     Price=models.IntegerField(null=True,blank=True)
#     Total_price=models.IntegerField(null=True,blank=True)
#     Book_image=models.ImageField(upload_to="cart_image",null=True,blank=True)

class cartDB1(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    FOOD_NAME = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    Total_price = models.IntegerField(null=True, blank=True)
    FOOD_IMAGE = models.ImageField(upload_to="food_catagory", null=True, blank=True)

class orderDB(models.Model):
        fullname = models.CharField(max_length=200)
        mobile = models.CharField(max_length=15)
        address = models.TextField()
        pincode = models.CharField(max_length=10)
        total_amount = models.IntegerField(null=True, blank=True)




