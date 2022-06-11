from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('companies/', views.getCompanies, name='getCompanies'),
    path('companies/<str:pk>', views.getCompany, name='company'),
    path('companies/<str:pk>/update/', views.updateCompany, name='update-company'),
]
