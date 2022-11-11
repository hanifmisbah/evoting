from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('adminPage/', views.loginPageAdmin, name='admin'),
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.regisPage, name='register'),
]