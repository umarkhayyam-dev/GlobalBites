from django.shortcuts import render, redirect
from admin_app.models import CatagoryDB,FoodDB
from webapp.models import SignupDB,ContactDB


# Create your views here.

def home_page_function(request):
    catagories=CatagoryDB.objects.all()
    foods=FoodDB.objects.all()
    return render(request,template_name="home.html",context={'catagories':catagories,'foods':foods})

def about_page_function(request):
    catagories = CatagoryDB.objects.all()
    return render(request,template_name="About.html",context={'catagories':catagories})

def contact_page_function(request):
    return render(request,template_name="Contact.html")

def save_contact(request):
    if request.method=="POST":
        name = request.POST.get('contact_name')
        email = request.POST.get('contact_email')
        subject = request.POST.get('contact_subjects')
        message = request.POST.get('contact_message')
        obj = ContactDB(CONTACT_NAME=name, CONTACT_EMAIL=email, CONTACT_SUBJECTS=subject, CONTACT_MESSAGE=message)
        obj.save()
        return redirect(contact_page_function)


def filter_page_function(request,food_cate):
    foods = FoodDB.objects.filter(FOOD_CATAGORY=food_cate)
    catagories = CatagoryDB.objects.all()
    return render(request,template_name="filter.html",context={'foods':foods,'catagories':catagories})

def single_page(request,food_id):
    foods_single= FoodDB.objects.get(id=food_id)
    catagories = CatagoryDB.objects.all()
    return render(request,template_name="single_page.html",context={'foods_single':foods_single,'catagories':catagories})

def signup_page(request):
    return render(request,template_name="signup.html")

def save_signup(request):
    if request.method=="POST":
        User=request.POST.get('Username')
        EMAIL=request.POST.get('email')
        PASSWORD=request.POST.get('passwoord')
        REAPEAT=request.POST.get('REAPEAT')
        PHONE=request.POST.get('phone')
        GENDER=request.POST.get('gender')
        objects=SignupDB(Username=User,Email=EMAIL,Password=PASSWORD,Repeate=REAPEAT,Phone=PHONE,Gender=GENDER)
        if SignupDB.objects.filter(Username=User).exists():
            return redirect(signup_page)
        elif SignupDB.objects.filter(Email=EMAIL).exists():
            return redirect(signup_page)
        else:

            objects.save()
            return redirect(signup_page)


def signin_page(request):
    if request.method=="POST":
        un=request.POST.get('email')
        pswd=request.POST.get('pass')
        user = SignupDB.objects.filter(Email=un, Password=pswd).first()
        if SignupDB.objects.filter(Email=un,Password=pswd).exists():
            request.session['Username'] = user.Username
            request.session['email']=un
            request.session['pass']=pswd
            return redirect(home_page_function)
        else:
            return redirect(signin_page)


    return render(request,template_name="signin.html")

def logout_function(request):
    del request.session['Username']
    del request.session['email']
    del request.session['pass']
    return redirect(signin_page)







