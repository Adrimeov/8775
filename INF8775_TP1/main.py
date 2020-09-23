import sys

from INF8775_TP1.closest_points.brute_force import execute_brute_force
from INF8775_TP1.closest_points.DpR import execute_DpR
from copy import deepcopy

NB_REP = 10

if __name__ == "__main__":

    file_name = ''

    if (len(sys.argv) <= 1):
        exit('Erreur: Pas assez d\'arguments. Vous devez indiquer le \
    nombre de points à générer et le nom du fichier de sortie.')

    if (len(sys.argv) > 2):
        exit('Erreur: Trop d\'arguments.')

    try:
        file_name = str(sys.argv[1])

        if file_name == "":
            raise ValueError()
    except:
        exit('Erreur: Le premier argument (nombre de points) doit être \
    un entier positif.')

    print(file_name)

    n = 0
    points = []

    with open(file_name, "r") as file:
        n = int(file.readline())

        for line in file:
            points.append(tuple([int(a) for a in line.split()]))

    points_x = deepcopy(points)
    points_x.sort(key=lambda tup: tup[0])
    points_y = deepcopy(points)
    points_y.sort(key=lambda tup: tup[1])

    average_time = 0

    for i in range(NB_REP):
        time = execute_DpR(points_x, points_y, 5)
        print("Run #" + str(i + 1) + ": " + str(time) + "s")
        average_time += time

    average_time /= NB_REP
    print("Average time: " + str(average_time) + "s")
