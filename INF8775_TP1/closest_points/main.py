import random
import math
import sys
import time
import csv

from brute_force import execute_brute_force
from DpR import execute_DpR
from utils import GRID_SIZE

ALGO = sys.argv[1] # Algo à utiliser DPR ou BF
NB_POINTS = int(sys.argv[2]) # Nombre de points à générer


'''
Un point est représenté par un tuple (position_x, position_y)
La fonction generate_points génère une liste de N points.
'''
def generate_points(N):
    points = [(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE)) for i in range(N)]
    return points

'''
--------------------------------------------------------------------
ATTENTION : Dans votre code vous devez utiliser le générateur gen.py
pour générer des points. Vous devez donc modifier ce code pour importer
les points depuis les fichiers générés.
De plus, vous devez faire en sorte que l'interface du tp.sh soit
compatible avec ce code (par exemple l'utilisation de flag -e, -a, (p et -t)).
--------------------------------------------------------------------
 '''

def main(algo, nb_points):
    POINTS = generate_points(nb_points)
    sorted_points_x = sorted(POINTS, key=lambda x: x[0])
    sorted_points_y = sorted(POINTS, key=lambda x: x[1])
    
    if algo == "BF":
        # Exécuter l'algorithme force brute
        time_BF = execute_brute_force(sorted_points_x)
        print("Temps : ", time_BF)
    
    elif algo == "DPR":
        # Exécuter l'algorithme Diviser pour régner
        SEUIL_DPR = 3
        time_DPR = execute_DpR(sorted_points_x, sorted_points_y, SEUIL_DPR)
        print("Temps : ", time_DPR)

main(ALGO, NB_POINTS)