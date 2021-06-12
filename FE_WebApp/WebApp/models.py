from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Employees (models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    salary = models.IntegerField()
    # position = models.CharField(max_length=64)
    # email = models.EmailField()
    # # contact_No = models.IntegerField()
    # # address = models.CharField(max_length=128)




    # def __str__(self):
    #     return (f"{self.id}: Name: {self.first_name} {self.last_name} \n Salary: {self.salary}")