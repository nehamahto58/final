from django.contrib import admin

# Register your models here.
from . models import doctor_profile
from .models import Symptoms
admin.site.register(doctor_profile)
admin.site.register(Symptoms)