from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(self):
    return HttpResponse("Coucou")
