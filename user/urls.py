from django.contrib import admin
from django.urls import path,include
from . import views


app_name="user"
urlpatterns = [
    path('login/',views.loginUser,name = "loginUser"),
    path('register/',views.registerUser,name = "registerUser"),
    path('logout/',views.logoutUser,name = "logoutUser"),
    path('profile/',views.userProfile,name = "userProfile"),
    path('edit/',views.editProfile,name = "editProfile"),


]