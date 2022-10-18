from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.regisPage, name='register'),
]