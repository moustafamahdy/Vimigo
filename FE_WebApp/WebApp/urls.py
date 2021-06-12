from django.http import request
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('Employees/', views.EmployeesList.as_view(), name="employees"),
    path('Employees/<int:pk>/', views.Employee.as_view(), name="employeedetail"),
    path('create/', views.CreateEmployee.as_view(), name="create"),
    path('Employees/<int:pk>/delete/', views.DeleteEmployee.as_view(), name="delete")

]