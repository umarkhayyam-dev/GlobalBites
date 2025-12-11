from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from admin_app.models import CatagoryDB,FoodDB
from webapp.models import ContactDB
from django.contrib import messages

import datetime

# Create your views here.

def index_function(request):
    catagory=CatagoryDB.objects.count()
    food=FoodDB.objects.count()
    date=datetime.datetime.now()
    return render(request,template_name="index.html",context={'catagory':catagory,'food':food})

def add_catagory(request):
    return render(request,template_name="add_catagory.html")

def save_catagory(request):
    if request.method=="POST":
        catogary_name=request.POST.get('catagory_name')
        catogary_image=request.FILES['catagory_image']
        catogary_description=request.POST.get('catagory_description')
        obj=CatagoryDB(NAME=catogary_name,IMAGE=catogary_image,DESCRIPTION=catogary_description)
        obj.save()
        messages.success(request,message="THE DATA HAS BEEN SAVED SUCCESSFULLY")
        return redirect(add_catagory)

def add_catagory_display(request):
    data=CatagoryDB.objects.all()
    return render(request,template_name="add_catagory_display.html",context={'data':data})

def add_catagory_edit(request,product_id):
    product=CatagoryDB.objects.get(id=product_id)

    return render(request,template_name="add_catagory_edit.html",context={'product':product})

def update_catagory(request,p_id):
    if request.method=="POST":
        catogary_name = request.POST.get('catagory_name')
        catogary_description = request.POST.get('catagory_description')
        try:
            img=request.FILES['catagory_image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CatagoryDB.objects.get(id=p_id).IMAGE
        CatagoryDB.objects.filter(id=p_id).update(NAME=catogary_name,IMAGE=file,DESCRIPTION=catogary_description)
        messages.success(request, message="UPDATED SUCCESS FULLY")
        return redirect(add_catagory_display)
def delete_catagory(request,pro_id):
    delete=CatagoryDB.objects.get(id=pro_id)
    delete.delete()
    messages.success(request, message="DELETED SUCCESS FULLY")
    return redirect(add_catagory_display)





def add_food(request):
    catagories=CatagoryDB.objects.all()
    return render(request,template_name="add_food.html",context={'catagories':catagories})

def save_add_food(request):
    if request.method=="POST":
        NAME=request.POST.get('food_name')
        PRICE=request.POST.get('food_price')
        CATAGORY=request.POST.get('food_catagory')
        FILE_UPLOAD=request.FILES['food_file']
        DESCRIPTION=request.POST.get('food_description')
        obj=FoodDB(FOOD_NAME=NAME,FOOD_CATAGORY=CATAGORY,FOOD_PRICE=PRICE,FOOD_DESCRIPTION=DESCRIPTION,FOOD_IMAGE=FILE_UPLOAD)
        obj.save()
        messages.success(request,message="NEW FOOD IS SAVED SUCCESSFULLY")
        return redirect(add_food)

def display_add_food(request):
    data=FoodDB.objects.all()
    return render(request,template_name="add_food_display.html",context={'data':data})

def edit_add_food(request,edit_id):
    products=FoodDB.objects.get(id=edit_id)
    return render(request,template_name="add_food_edit.html",context={'products':products})

def update_food(request,update_id):
    if request.method=="POST":
        NAME = request.POST.get('food_name')
        PRICE = request.POST.get('food_price')
        CATAGORY = request.POST.get('food_catagory')
        DESCRIPTION = request.POST.get('food_description')
        try:
            img=request.FILES['food_file']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=FoodDB.objects.get(id=update_id).FOOD_IMAGE
        FoodDB.objects.filter(id=update_id).update(FOOD_NAME=NAME,FOOD_CATAGORY=CATAGORY,FOOD_PRICE=PRICE,FOOD_DESCRIPTION=DESCRIPTION,FOOD_IMAGE=file)
        messages.success(request,message="FOOD HAS UPDATED")
        return redirect(display_add_food)

def delete_food(request,pro_id):
    delete_food=FoodDB.objects.get(id=pro_id)
    delete_food.delete()
    messages.success(request, message="DELETED SUCCESS FULLY")
    return redirect(display_add_food)

def login_function(request):
    return render(request,template_name="login.html")




def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pswd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            data=authenticate(username=un,password=pswd)
            if data is not None:
                login(request,data)
                request.session['username']=un
                request.session['password']=pswd
                return redirect(index_function)
            else:
                return redirect(login_function)
        else:
            return redirect(login_function)



def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_function)

def message_function(request):
    data=ContactDB.objects.all()
    return render(request,template_name="Message_function.html", context={'data':data})

def delete_message(request,p_id):
    contact_data=ContactDB.objects.get(id=p_id)
    contact_data.delete()
    return redirect(message_function)




