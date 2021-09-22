from django.db import models

class Stop(models.Model):
    
    id = models.IntegerField(("id"), primary_key=True)
    nom = models.CharField(("nom"), max_length=200)
    desserte = models.CharField(("desserte"), max_length=200)
    pmr = models.BooleanField(("pmr"), default=False)
    ascenseur = models.BooleanField(("ascenseur"), default=False)
    escalator = models.BooleanField(("escalator"), default=False)
    gid = models.IntegerField(("gid"), default=False)
    last_update = models.DateTimeField(("last_update"), max_length=200)
    last_update_fme = models.DateTimeField(("last_update_fme"), max_length=200)
    coord1 = models.DecimalField(("coord1"), max_digits = 45, decimal_places = 20)
    coord2 = models.DecimalField(("coord2"), max_digits = 45, decimal_places = 20)

    def __str__(self):
        return self.nom