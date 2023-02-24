from django.contrib import admin
from .models import Profile, Employees, Shifts, ShiftsEmployees

# Register your models here.
admin.site.register(Profile)
admin.site.register(Employees)
admin.site.register(Shifts)
admin.site.register(ShiftsEmployees)