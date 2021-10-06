# TCL Project

## Contexte
À l’horizon 2022, il peut être encore pénible de se déplacer dans l’agglomération Lyonnaise si l’on se trouve dans une situation d’handicap temporaire ou définitive. 

En effet le cas échéant, il est nécessaire de bénéficier d’infrastructures adaptées telles que : les rampes d’embarquement (disponibles sur certains bus), d’escalator, d’ascenseur (à proximité des arrêts afin d’éviter les escaliers) etc… 

Partant de ce constat, nous avons entrepris de construire un service offrant la possibilité aux personnes précitées de localiser de tels arrêts.  

## Hébergement:
Afin d'héberger le site en local, il est nécessaire de :
 - Télécharger Django par pip : python -m pip install Django
 - Lancer ledit serveur depuis tcl-project/manage.py : python manage.py runserver
 - Comme dit dans la console, le site est joignable depuis [ici](http://127.0.0.1:8000)

 ### Attention ! 
 Certains navigateurs force la connexion via https alors que le serveur local ne supporte pas les certificats du serveur hébergeant la version de déploiement.
 -> Solution : Désactiver cette fonctionnalité ou utiliser un autre navigateur tel que Mozilla Firefox
