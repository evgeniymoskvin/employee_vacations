from django.contrib import admin
from .models import EmployeeModel, VacationsModel

# Register your models here.

admin.site.register(EmployeeModel)
admin.site.register(VacationsModel)