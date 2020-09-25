import sys
import argparse
from closest_points.brute_force import execute_brute_force
from closest_points.DpR import execute_DpR
from copy import deepcopy

NB_REP = 10


def execute_closest_points(path=None, algo="recursif", timer=False, distance=False):
    points = []
    algo_dictionary = {"recursif": execute_DpR, "brute": execute_brute_force}
    with open(path, "r") as file:
        file.readline()
        for line in file:
            points.append(tuple([int(a) for a in line.split()]))

    points_x = deepcopy(points)
    points_x.sort(key=lambda tup: tup[0])
    points_y = deepcopy(points)
    points_y.sort(key=lambda tup: tup[1])

    time, min_dpr = algo_dictionary[algo](points_x, points_y, 5)

    if bool(timer):
        print("Time to compute: " + str(time) + "s")
    if distance:
        print("Minimal distance: " + str(min_dpr) + "s")

    return time


if __name__ == "__main__":

    file_name = ""

    if (len(sys.argv) <= 1):
        exit('Erreur: Pas assez d\'arguments. Vous devez indiquer le \
              nombre de points à générer et le nom du fichier de sortie.')

    arguments = ["--path", "--timer", "--algo", "--distance"]
    parser = argparse.ArgumentParser()

    for argument in arguments:
        parser.add_argument(argument)

    args = parser.parse_args()
    args_as_dict = vars(args)
    parameters = {a: vars(args)[a] for a in vars(args) if vars(args)[a] != ""}
    execute_closest_points(**parameters)
