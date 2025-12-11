from django.shortcuts import render, redirect
from admin_app.models import CatagoryDB,FoodDB
from webapp.models import cartDB1,orderDB
from webapp.models import SignupDB,ContactDB
import razorpay


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

def cart_page(request):
    cart_data = cartDB1.objects.filter(Username=request.session['Username'])
    cart_total = 0
    uname = request.session.get('Username')
    if uname:
        cart_total = cartDB1.objects.filter(Username=uname).count()

        sub_total = 0
        deliver_charge = 0
        total_amount = 0
        for i in cart_data:
            sub_total += i.Total_price
            if sub_total > 500:
                deliver_charge = 50
            else:
                deliver_charge = 100
            total_amount = sub_total + deliver_charge
    return render(request,template_name="cart_page.html",context={"cart_data": cart_data,'cart_total':cart_total,'sub_total':sub_total,'deliver_charge':deliver_charge,'total_amount':total_amount})

def checkout_page(request):
    cart_total = 0
    cart_data = cartDB1.objects.filter(Username=request.session['Username'])
    uname = request.session.get('Username')
    if uname:
        cart_total = cartDB1.objects.filter(Username=uname).count()

        sub_total = 0
        deliver_charge = 0
        total_amount = 0
        for i in cart_data:
            sub_total += i.Total_price
            if sub_total > 500:
                deliver_charge = 50
            else:
                deliver_charge = 100
            total_amount = sub_total + deliver_charge
    return render(request,template_name="checkout.html",context={'cart_total':cart_total,'sub_total':sub_total,'deliver_charge':deliver_charge,'total_amount':total_amount})

def order_confirm(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        pincode = request.POST.get("pincode")
        total_amount = request.POST.get("total_amount")  # taking from form

        # Save into orderDB
        obj = orderDB(
            fullname=fullname,
            mobile=mobile,
            address=address,
            pincode=pincode,
            total_amount=total_amount
        )
        obj.save()

        return redirect('payment')

    return redirect('checkout_page')



def add_to_cart(request, food_id):
    if request.method == "POST":
        # Logged in user from session
        username_cart = request.session.get("Username")

        # Fetch food details using ID
        food = FoodDB.objects.get(id=food_id)

        # Get quantity from form
        quantity_cart = int(request.POST.get("quantity"))
        price_cart = food.FOOD_PRICE
        total_cart = quantity_cart * price_cart

        # Save to cart table
        obj = cartDB1(
            Username=username_cart,
            FOOD_NAME=food.FOOD_NAME,
            quantity=quantity_cart,
            price=price_cart,
            Total_price=total_cart,
            FOOD_IMAGE=food.FOOD_IMAGE
        )
        obj.save()

        return redirect('cart_page')

def payment(request):

        catagories = CatagoryDB.objects.all()

        cart_total = 0
        uname = request.session.get('Username')
        if uname:
            cart_total = cartDB1.objects.filter(Username=uname).count()

            customer = orderDB.objects.order_by('-id').first()

            payy = customer.total_amount
            amount = int(payy * 100)
            payy_str = str(amount)

            if request.method == "POST":
                order_currency = 'INR'
                client = razorpay.Client(auth=('rzp_test_0ib0jPwwZ7I1lT', 'VjHNO5zKeKxz8PYe7VnzwxMR'))
                payment = client.order.create({'amount': amount, 'currency': order_currency})
        return render(request, template_name="payment.html",
                      context={'catagories': catagories, 'cart_total': cart_total, 'payy_str': payy_str})









