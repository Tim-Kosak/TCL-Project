from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .tools import *
from decimal import Decimal

# Create your views here.

def index(request):
    return render(request, 'index.html', {"port" : request.META['SERVER_PORT']})

def getRoute(request):
    stop_list = Stop.objects.filter(coord1__lte = 1000, coord2__lte = 1000) #Filtre sur les adresses non valides

    lat = Decimal(request.GET.get("lat"))
    lon = Decimal(request.GET.get("lon"))

    id_res = get_nearset_stop(stop_list, lat, lon)

    context = {
        "stop_list" : stop_list,
        "lat" : lat,
        "lon" : lon,
        "nearest_stop" : Stop.objects.get(id=id_res),
        "research_parameters" : ["P.M.R", "Escalator", "Ascenceur"]
    }
    return render(request, 'getRoute.html', context )