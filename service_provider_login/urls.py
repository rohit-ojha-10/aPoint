from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('sRegister',views.sRegister,name='sRegister'),
    path('service_register',views.service_register,name='service_register'),
    path('service_login',views.service_login,name='service_login'),
    path('service_home',views.service_home,name='service_home'),
    path('Slogout',views.Slogout,name='Slogout'),
    path('service_list',views.serviceList,name='service_list'),
    path('update_slots',views.updateSlots,name='update_slots'),
    path('sLogin',views.sLogin,name='sLogin'),
    path('select',views.select,name='select')
]
