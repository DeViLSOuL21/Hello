from django.http import HttpResponse
from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import *

# Create your views here.
def index(request):
    context={
        'variable':"this is sent"
            }
    return render(request, 'index.html',context)
    
    # return HttpResponse('This is Homepage')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('Kirti will letuk about the about page')

def enrollment(request):
    return render(request, 'enrollment.html')
    #return HttpResponse('Kumar will letuk about the services page')

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse('Yash will letuk about the contact page')

def add_volunteer(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Department = request.POST.get('Department')
        Phone = request.POST.get('Phone')
        Volunteer_as = request.POST.get('Volunteer_as')
        print(Name,Email,Phone,Volunteer_as)
    
        Volunteer.objects.create(Email=Email, Phone=Phone, Volunteer_as=Volunteer_as, date=datetime.today(),Name = Name, Department=Department)
          # Redirect to a success URL after saving
    return render(request, 'volunteer.html')

from django.shortcuts import redirect

def add_alumnis(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        Department = request.POST.get('Department')
        Abroad = request.POST.get('Abroad')
        Alumni.objects.create(Name=Name, Email=Email, Phone=Phone, Department=Department, Abroad=Abroad)
          # Redirect to a success URL after saving
    return render(request, 'alumni.html')


def add_registrations(request):

    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Department = request.POST.get('Department')
        Options = request.POST.get('Options')
        preference= request.POST.get('preference')
        print(Name,Email,Department,Options,preference)
        Registration.objects.create(Email=Email,Department=Department,Name=Name,preference=preference,date=datetime.today())
        
          # Redirect to a success URL after saving
    return render(request, 'registration.html')  



