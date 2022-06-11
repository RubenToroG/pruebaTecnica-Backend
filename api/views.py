from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Company
from .serializers import CompanySerializer
from api import serializers

@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {
            'Endpoint': '/company/',
            'method': 'GET',
            'body': None,
            'description': 'Get all companies'
        },
                {
            'Endpoint': '/company/id/',
            'method': 'GET',
            'body': None,
            'description': 'Get company by id'
        },
        {
            'Endpoint': '/company/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Get all companies'
        },
        {
            'Endpoint': '/company/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Update company info'
        },
        {
            'Endpoint': '/company/id/delete/',
            'method': 'DELETE',
            'body': "",
            'description': 'Delete company'
        },
    ],

    return Response(routes)

@api_view(['GET'])
def getCompanies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCompany(request, pk):
    companies = Company.objects.get(id=pk)
    serializer = CompanySerializer(companies, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateCompany(request, pk):
    data = request.data
    company = Company.objects.get(id=pk)
    serializer = CompanySerializer(instance=company, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)