from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('Cregister', views.Cregister, name='Cregister'),
    path('clogin', views.clogin, name='clogin'),
    path('consumer_login',views.consumer_login,name='consumer_login'),
    path('consumer_home', views.consumer_home, name='consumer_home'),
    path('logout', views.logout, name='logout')
]
