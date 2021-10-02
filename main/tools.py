import math
from .models import *

def dist(P1, P2):
    return math.sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)

def get_nearset_stop(stop_list, orig_lat, orig_lon):
    res_id = 0
    min_dist = dist([orig_lat, orig_lon], [stop_list[0].coord1, stop_list[0].coord2])

    
    for s in stop_list:
        distance = dist([orig_lat, orig_lon], [s.coord1, s.coord2])

        if min_dist > distance:
            res_id = s.id
            min_dist = distance
            #print("Nouvel arrêt trouvé : " + s.nom)

    return res_id