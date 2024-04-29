from django.http import HttpResponse
from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Volunteer
from home.models import Alumni
from home.models import Registration

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
    
        vi = Volunteer(Email=Email, Phone=Phone, Volunteer_as=Volunteer_as, date=datetime.today(),Name = Name, Department=Department)
        vi.save()
          # Redirect to a success URL after saving
    return render(request, 'volunteer.html')

def add_alumnis(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        Department = request.POST.get('Department')
        Abroad = request.POST.get('Department')


        alumni_instance = Alumni(Name=Name, Email=Email,Phone=Phone,Department=Department,Abroad=Abroad)
        alumni_instance.save()
        
        return ('success_url')  # Redirect to a success URL after saving
    return render(request, 'alumni.html')

def add_registrations(request):

    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Department = request.POST.get('Department')
        Options = request.POST.get('Options')
        preference= request.POST.get('preference')

        registration= Registration(
            Email=Email,
            Department=Department,
            Options=Options,
            Name=Name,
            preference=preference
        )
        
        registration.save()
          # Redirect to a success URL after saving
    return render(request, 'registration.html')  



