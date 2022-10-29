from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import ServiceCreds, ServiceCredsForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.forms import * 
# Create your views here.
def select(request):
    check=request.GET.get('name')
    if(check=='consumer'):
        return redirect('consumer_login')
    else:
        return redirect('sLogin')
def sLogin(request):
    return render(request,'service_login.html')
def sRegister(request):
     return render(request,'service_register.html')
def service_register(request):
    try:
        form=ServiceCredsForm(request.POST,request.FILES)
        form.save()
        return redirect('sLogin')
    except Exception as e:
        print(e)
        messages.info(request,'Username in use already')
        return render(request,'service_register.html')
def service_home(request):
    user=request.session.get('service_session')
    username=user
    detail=ServiceCreds.objects.get(user_name=username)
    print(detail)
    slots=detail.total_slots
    return render(request,"service_home.html",{'slots':slots})
def service_login(request):
    if(request.session.get('serivice_session')!=None):
        return redirect('service_home')
    user_name=request.POST['sUname']
    password=request.POST['sPassword']
    Creds=ServiceCreds.objects.all()
    for cred in Creds:
        if(cred.user_name == user_name and cred.password == password):
            request.session['service_session']=user_name
            return redirect('service_home')
    messages.info(request,"Credentials Invalid")
    request.session['check']='two'
    return redirect('sLogin')
def Slogout(request):
    del request.session['service_session']
    return redirect('/')

def serviceList(request):
    Type=request.GET.get('type')
    Service=ServiceCreds.objects.filter(service=Type)
    return render(request,'service_provider.html',{'Service':Service})
def updateSlots(request):
    slots=request.GET['slots_left']
    username=request.session.get('service_session')
    provider_creds=ServiceCreds.objects.get(user_name=username)
    provider_creds.total_slots=slots
    provider_creds.save()
    return redirect('service_home')

