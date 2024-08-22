from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import reg
# Create your views here.

def index(request):
    return render(request,"index.html")

def Register(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        insertdata=reg.objects.create(name=name,email=email,password=password)
        if insertdata:
            return redirect("/login/")
    else:
        return render(request,"register.html")

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST["password"]
        if email=="" and password=="":
            return HttpResponse("All fields mandatory")
        else:
            logindata=reg.objects.filter(email=email,password=password)
            if logindata:
                return redirect("/home/")
            else:
                return HttpResponse("Invalid username and password")
    else:
        return render(request,"login.html")    
    
def home(request):
    return render(request,"home.html")

def logout(request):
    return redirect('/admin/')
