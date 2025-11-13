from django.db import models



# Create your models here.

class CatagoryDB(models.Model):
    NAME= models.CharField(max_length=100,null=True,blank=True)
    IMAGE=models.ImageField(upload_to="Catagory",null=True,blank=True)
    DESCRIPTION=models.CharField(max_length=100,null=True,blank=True)

class FoodDB(models.Model):
    FOOD_NAME=models.CharField(max_length=100,null=True,blank=True)
    FOOD_CATAGORY=models.CharField(max_length=100,null=True,blank=True)
    FOOD_PRICE=models.IntegerField(null=True,blank=True)
    FOOD_DESCRIPTION=models.CharField(max_length=100,null=True,blank=True)
    FOOD_IMAGE=models.ImageField(upload_to="food_catagory",null=True,blank=True)

