from django.db import models

from decimal import *

import requests
import urllib.parse

class Stop(models.Model):
    
    id = models.IntegerField(("id"), primary_key=True)
    nom = models.CharField(("nom"), max_length=200)
    desserte = models.CharField(("desserte"), max_length=200)
    pmr = models.BooleanField(("pmr"), default=False)
    ascenseur = models.BooleanField(("ascenseur"), default=False)
    escalator = models.BooleanField(("escalator"), default=False)
    gid = models.IntegerField(("gid"))
    last_update = models.DateTimeField(("last_update"), max_length=200)
    last_update_fme = models.DateTimeField(("last_update_fme"), max_length=200)
    coord1 = models.DecimalField(("coord1"), max_digits = 45, decimal_places = 20)
    coord2 = models.DecimalField(("coord2"), max_digits = 45, decimal_places = 20)

    def __str__(self):
        return self.nom

    def updateCoords(self):
        url = 'https://nominatim.openstreetmap.org/search.php?q=' + urllib.parse.quote_plus(self.nom + ', Lyon') +'&format=jsonv2'

        response = requests.get(url).json()

        try:
            print(self.__str__() + str(self.id))
            self.coord1 = Decimal(response[0]["lat"])
            self.coord2 = Decimal(response[0]["lon"])
            self.save()
        except Exception:
            pass