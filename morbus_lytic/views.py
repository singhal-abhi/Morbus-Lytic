from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render,redirect,HttpResponseRedirect
import messages

from .models import UserManager,User

def index(request):
    return render(request,'index.html',{})

def simulation(request):
    print(1)
    return render(request,'simulation.html',{})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password,email=email)
        return login(request)
    return HttpResponseRedirect('/')

def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request,user)
                print("logged in as",user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Invalid Credentials')
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return redirect('/')
        except Exception as identifier:
            messages.error(request, 'Invalid Credentials')
            # print("******\n",identifier,1,"\n******",46)
            return redirect('/')
    else:
        return redirect('/')

def logout(request):
	request.session.flush()
	auth_logout(request)
	return redirect('/')