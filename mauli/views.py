from django.shortcuts import render,HttpResponse
from mauli.admin import Contact
from mauli.admin import Order

from django.shortcuts import render,redirect;
from datetime import datetime;
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,"index.html")

def contact(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        phoneno=request.POST.get('phoneno')
        email=request.POST.get('email')
        comment=request.POST.get('comment')
        contacts=Contact(firstname=firstname,lastname=lastname,phoneno=phoneno,email=email,comment=comment)
        contacts.save()
       
    return render(request,"contact.html")

def order(request):
    if request.method=="POST":
        crop=request.POST.get('crop')
        quantity=request.POST.get('quantity')
        date=request.POST.get('date')
        fullname=request.POST.get('fullname')
        phoneno=request.POST.get('phoneno')
        address=request.POST.get('address')
        order=Order(crop=crop,quantity=quantity,phoneno=phoneno,date=date,fullname=fullname,address=address)
        order.save()
    return render(request,"order.html")

def about(request):
    return render(request,"about.html")

def cucumber(request):
    return render(request,"cucumber.html")

def bringle(request):
    return render(request,"bringle.html")

def brocoli(request):
    return render(request,"brocoli.html")

def cabbage(request):
    return render(request,"cabbage.html")

def chilli(request):
    return render(request,"chilli.html")

def flower(request):
    return render(request,"flower.html")

def marigold(request):
    return render(request,"marigold.html")

def watermelon(request):
    return render(request,"watermelon.html")

def tomato(request):
    return render(request,"tomato.html")

def sugarcane(request):
    return render(request,"sugarcane.html")

def bittergourd(request):
    return render(request,"bittergourd.html")
    
    
    