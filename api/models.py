from turtle import update
from django.db import models

class Company(models.Model):
    name = models.models.CharField(max_length=100)
    address = models.models.CharField(max_length=100)
    phone = models.models.CharField(max_length=20)
    nit = models.models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name