from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.reverse import reverse
from .models import Employees
from .serializers import EmployeesSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import HTMLFormRenderer, TemplateHTMLRenderer
from django.http import Http404
from rest_framework import mixins, generics


class EmployeesList(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "employees/EmployeesList.html"

    
    def get(self, request):
        queryset = Employees.objects.all()

        return Response({
            "employees": queryset
        })



class CreateEmployee(mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

    def post(self, request):
        self.create(request)
        return HttpResponseRedirect(reverse('employees'))
    


class Employee(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "employees/Employee.html"

    def get(self, request, pk):
        employee = get_object_or_404(Employees, pk= pk)
        serializer = EmployeesSerializer(employee)

        return Response({
            "serializer": serializer,
            "employee": employee
        })

    def post(self, request, pk):
        employee = get_object_or_404(Employees, pk= pk)
        serilaizer = EmployeesSerializer(employee, data= request.data)

        if not serilaizer.is_valid():
            return Response({
                "serializer": serilaizer,
                 "employee": employee
            }, status= status.HTTP_202_ACCEPTED)

        serilaizer.save()
        return redirect("employees")

class DeleteEmployee(APIView):

    def  get_Employee(self, pk):
        try:
            return Employees.objects.get(pk= pk)
        except Employees.DoesNotExist:
            raise Http404

    def delete(self, request, pk, *args):
        employee = self.get_Employee(pk)
        employee.delete()
        return HttpResponseRedirect(reverse('employees'))

