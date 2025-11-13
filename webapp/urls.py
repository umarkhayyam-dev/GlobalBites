from django.urls import path
from webapp import views

urlpatterns=[
    path('home_page_function/',views.home_page_function,name="home_page_function"),
    path('about_page_function/',views.about_page_function,name="about_page_function"),
    path('contact_page_function/',views.contact_page_function,name="contact_page_function"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('filter_page_function/<food_cate>',views.filter_page_function,name="filter_page_function"),
    path('single_page/<int:food_id>/',views.single_page,name="single_page"),
    path('signup_page/',views.signup_page,name="signup_page"),
    path('signin_page/',views.signin_page,name="signin_page"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('logout_function/',views.logout_function,name="logout_function"),







]