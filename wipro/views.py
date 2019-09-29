from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import employeedetails
from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
def empoyeeList(APIView):
    def get(self,request):
        employee1=employeedetails.objects.all()
        return response