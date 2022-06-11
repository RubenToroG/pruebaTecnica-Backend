from django.shortcuts import render
from django.http import JsonResponse

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
    ]

    return JsonResponse(routes, safe=False)