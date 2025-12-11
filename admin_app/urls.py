from django.urls import path
from admin_app import views

urlpatterns=[
    path('index_function/',views.index_function,name="index_function"),
    path('add_catagory/',views.add_catagory,name="add_catagory"),
    path('save_catagory/',views.save_catagory,name="save_catagory"),
    path('add_catagory_display/',views.add_catagory_display,name="add_catagory_display"),
    path('add_catagory_edit/<int:product_id>/',views.add_catagory_edit,name="add_catagory_edit"),
    path('update_catagory/<int:p_id>/',views.update_catagory,name="update_catagory"),
    path('delete_catagory/<int:pro_id>/',views.delete_catagory,name="delete_catagory"),



    path('add_food/',views.add_food,name="add_food"),
    path('save_add_food/',views.save_add_food,name="save_add_food"),
    path('display_add_food/',views.display_add_food,name="display_add_food"),
    path('edit_add_food/<int:edit_id>/',views.edit_add_food,name="edit_add_food"),
    path('update_food/<int:update_id>/',views.update_food,name="update_food"),
    path('delete_food/<int:pro_id>/',views.delete_food,name="delete_food"),

    path('login_function/',views.login_function,name="login_function"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    path('message_function/',views.message_function,name="message_function"),
    path('delete_message/<int:p_id>/',views.delete_message,name="delete_message"),
















]