from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("enrollment", views.enrollment, name='enrollment'),
    path("contact", views.contact, name='contact'),
    path("volunteer", views.add_volunteer, name='volunteer'),
    path("alumni", views.add_alumnis, name="alumni"),
    path("registration", views.add_registrations, name="registration"),
]
