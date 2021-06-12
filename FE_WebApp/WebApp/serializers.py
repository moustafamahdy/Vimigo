from django.db.models import fields
from django.db.models.fields import files
from rest_framework import serializers
from .models import Employees

class EmployeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        # fields = ('fist_name', 'last_name')
        fields = '__all__'

    def validate(self, attrs):
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)