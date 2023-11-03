from .models import Service
from django.shortcuts import render

def services(request):
    services = Service.objects.all()
    return {'services': services}