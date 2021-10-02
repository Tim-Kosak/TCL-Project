from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .tools import *
from decimal import Decimal
from django.urls import reverse

# Create your views here.

addr = "https://tcl-groupe-3.webredirect.org:"

# Vue web récupérant les coordonnées GPS de l'utilisateur
def index(request):
    return render(request, 'index.html', {"port" : request.META['SERVER_PORT'],
                                           "siteaddr" : addr })

# Vue affichant le fond de carte avec l'itinéraire vers l'arrêt le plus proche
def getRoute(request):

    # Récupère les paramètres passés par GET
    esc_param = str(request.GET.get("Escalator"))
    pmr_param = str(request.GET.get("P.M.R"))
    asc_param = str(request.GET.get("Ascenseur"))

    stop_list = Stop.objects.filter(coord1__lte = 1000, coord2__lte = 1000) #Filtre sur les adresses non valides, i.e latitude / longitude > 1000

    print("Total stop_list size (Before): " + str(stop_list.count()))

    # Filter none-escalator bus Stop
    if esc_param.__contains__("with"):
        stop_list = stop_list.filter(escalator=1)

    # '' none-elevator ''
    if asc_param.__contains__("with"):

        stop_list = stop_list.filter(ascenseur=1)

    #'' none-pmr ''
    if pmr_param.__contains__("with"):
        stop_list = stop_list.filter(pmr=1)
        
    print("Total stop_list size (After): " + str(stop_list.count()))

    lat = Decimal(request.GET.get("lat"))
    lon = Decimal(request.GET.get("lon"))

    #Détermine l'arrêt de bus le plus proche depuis la list filtrée fournie
    id_res = get_nearset_stop(stop_list, lat, lon)

    print([["P.M.R",pmr_param], ["Escalator", esc_param], ["Ascenseur", asc_param]])

    #Contexte passé lors du rendu
    context = {
        "stop_list" : stop_list,
        "lat" : lat,
        "lon" : lon,
        "nearest_stop" : Stop.objects.get(id=id_res),
        "navBar_research_parameters" : [["P.M.R",pmr_param], ["Escalator", esc_param], ["Ascenseur", asc_param]],
        "site_addr" : addr + request.META['SERVER_PORT'] + reverse("getRoute")
    }

    return render(request, 'getRoute.html', context )