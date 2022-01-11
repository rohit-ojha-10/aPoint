from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import ConsumerCreds
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    if(request.session.get('check') == None):
        request.session['check'] = 'one'
    return render(request, 'index.html')


def Cregister(request):
    return render(request, 'Cregister.html')


def consumer_home(request):
    return render(request, 'consumer_home.html')
    
def register(request):
    Creds = ConsumerCreds.objects.all()
    full_name = request.GET['full_name']
    username = request.GET['username']
    password = request.GET['password']
    if ConsumerCreds.objects.filter(username=username).exists():
        messages.info(request, 'Username in use')
        return redirect('Cregister')
    else:
        user = ConsumerCreds(full_name=full_name,
                             password=password, username=username)
        user.save()
        return redirect('consumer_login')

def logout(request):
    if(request.session.get('consumer_session')!=None):
        del request.session['consumer_session']
    return redirect('/')


def consumer_login(request):
    return render(request,'consumer_login.html')


def clogin(request):
    if(request.session.get('consumer_session') != None):
        return redirect('consumer_home')
    username = request.GET['cUsername']
    password = request.GET['cPassword']
    Creds = ConsumerCreds.objects.all()
    for cred in Creds:
        if cred.username == username and cred.password == password:
            request.session['consumer_session'] = username
            return render(request, 'consumer_home.html')

    messages.info(request, 'Credentials dont match')
    request.session['check'] = 'one'
    return redirect('consumer_login')
