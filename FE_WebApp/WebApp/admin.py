# from FE_WebApp.WebApp.models import Employees
from django.contrib import admin
from .models import Employees
# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "salary")


admin.site.register(Employees, EmployeesAdmin)