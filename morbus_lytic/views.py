from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html',{})

def simulation(request):
    print(1)
    return render(request,'simulation.html',{})