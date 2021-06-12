from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django import template
from rest_framework.serializers import LIST_SERIALIZER_KWARGS
from .models import Employees
from .serializers import EmployeesSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import HTMLFormRenderer, TemplateHTMLRenderer
from django.http import Http404
from rest_framework import mixins, generics,viewsets


class EmployeesList(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "employees/EmployeesList.html"
    # queryset = Employees.objects.all()
    # serializer_class = EmployeesSerializer

    
    def get(self, request):
        queryset = Employees.objects.all()

        return Response({
            "employees": queryset
        })

    # @LIST_SERIALIZER_KWARGS
    
    # def blank_form(self, request, *args, **kwargs):
    #     # employee = get_object_or_404(Employees, pk= pk)
    #     # self.object = self.g
        
    #     serilaizer = EmployeesSerializer()
        


    #     if not serilaizer.is_valid():
    #         return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST) 

    #     serilaizer.save()
    #     return Response({
    #             # "serializer": serilaizer
    #             # # "employee": employee
    #         }, status= status.HTTP_201_CREATED)
        


class CreateEmployee(mixins.CreateModelMixin, generics.GenericAPIView):
    # queryset = Employees.objects.all()
    # serializer_class = EmployeesSerializer
    # template_name = 'employees/CreateEmployee.html'
    # renderer_classes = [TemplateHTMLRenderer]

    # def blank_form(self, request, *args):
    #     serializer = EmployeesSerializer()
    #     return Response({
    #         "serializer": serializer
    #     })

    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

    def post(self, request):

        return self.create(request)
    


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
            })

        serilaizer.save()
        return redirect("employees")
# class EmployeesList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

#     queryset = Employees.objects.all()
#     serializer_class = EmployeesSerializer

#     def get(self, request):
#         return self.list(request)
#         # return self.list(request), render(request, "employees/EmployeesList.html", {
#         #     "employees": Employees.objects.all()
#         # })
        
#     def sasa(self, request):
        
#         ListOfEmployees = self.list(request)
#         employees = Employees.objects.all()
#         serializer = EmployeesSerializer(employees, many= True)
#         return render(request, "employees/EmployeesList.html", {

#             "employees": serializer.data
            

#         })

#     def post(self, request):
#         return self.create(request)


# class Employee(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

#     queryset = Employees.objects.all()
#     serializer_class = EmployeesSerializer

#     def get(self, request, pk):

#         return self.retrieve(request)
#     def put(self, request, pk):

#         return self.update(request)

#     def delete(self, request, pk):
        
#         return self.destroy(request)







# @api_view(['GET', 'POST'])

# def EmployeesList(request):
#     if request.method == 'GET':
#         Employees_List = Employees.objects.all() # to get list of Employees
#         serializer = EmployeesSerializer(Employees_List, many=True) # to serialize the Employee list
#         return Response(serializer.data) # to return the Data to the user in Json format 

#     if request.method == 'POST':
#         # to give the data to the serializer
#         serializer = EmployeesSerializer(data = request.data)
#         # to check if all the required field exist 
#         if serializer.is_valid():
#             serializer.save()
#             # to return the data to the user and tell him that the object is successfully created
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         else:
#             # return error for the user which means that the request is not valid
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def Employee (request, id):
#     try:
#         employee = Employees.objects.get(pk = id)
#     except Employees.DoesNotExist:
#         return Response(status = 404)

#     if request.method == 'GET':
#         serializer = EmployeesSerializer(employee)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         serializer = EmployeesSerializer(employee, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         employee.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
