from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .tools import *
from decimal import Decimal
from django.urls import reverse

# Create your views here.

addr = "http://127.0.0.1:"

def index(request):
    return render(request, 'index.html', {"port" : request.META['SERVER_PORT']})

def getRoute(request):
    stop_list = Stop.objects.filter(coord1__lte = 1000, coord2__lte = 1000) #Filtre sur les adresses non valides

    lat = Decimal(request.GET.get("lat"))
    lon = Decimal(request.GET.get("lon"))

    id_res = get_nearset_stop(stop_list, lat, lon)

    print([["P.M.R",request.GET.get("P.M.R")], ["Escalator", str(request.GET.get("Escalator"))], ["Ascenceur", request.GET.get("Ascenceur")]])

    context = {
        "stop_list" : stop_list,
        "lat" : lat,
        "lon" : lon,
        "nearest_stop" : Stop.objects.get(id=id_res),
        "navBar_research_parameters" : [["P.M.R",request.GET.get("P.M.R")], ["Escalator", request.GET.get("Escalator")], ["Ascenceur", request.GET.get("Ascenseur")]],
        "site_addr" : addr + request.META['SERVER_PORT'] + reverse("getRoute")
    }
    return render(request, 'getRoute.html', context )