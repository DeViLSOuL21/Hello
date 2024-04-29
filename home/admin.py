from django.contrib import admin
from home.models import Volunteer
from home.models import Alumni
from home.models import Registration

# Register your models here.
admin.site.register(Volunteer)
admin.site.register(Alumni)
admin.site.register(Registration)