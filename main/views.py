from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    stop_list = Stop.objects.get(pmr=True)
    return render(request, 'index.html', {"stop_list" : stop_list} )
