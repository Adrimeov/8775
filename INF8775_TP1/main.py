import sys
import argparse
from closest_points.brute_force import execute_brute_force
from closest_points.DpR import execute_DpR
from copy import deepcopy
import closest
import time
NB_REP = 10


def py_points_to_cpp_points(points):
    cpp_points = []
    for point in points:
        x, y = point
        cpp_point = closest.Point(int(x), int(y))
        cpp_points.append(cpp_point)

    return cpp_points


def extract_points_from_file(path):
    points = []
    with open(path, "r") as file:
        file.readline()
        for line in file:
            points.append(tuple(int(a) for a in line.split()))

    return points, len(points)


def execute_closest_points(path=None, algo="brute", timer=False, distance=False, recursion=5):
    algo_dictionary = {"brute": closest.call_brute_force, "recursif": closest.call_recursive}
    python_points, nb_points = extract_points_from_file(path)
    points_x = deepcopy(python_points)
    points_x.sort(key=lambda tup: tup[0])
    points_y = deepcopy(python_points)
    points_y.sort(key=lambda tup: tup[1])
    cpp_points_x = py_points_to_cpp_points(points_x)
    cpp_points_y = py_points_to_cpp_points(points_y)

    start = time.time()
    min_dpr = algo_dictionary[algo](cpp_points_x, cpp_points_y, recursion, nb_points)
    end = time.time()

    if bool(timer):
        print("Time to compute: " + str(end - start) + "s")
    if distance:
        print("Minimal distance: " + str(min_dpr) + "s")

    return time


if __name__ == "__main__":

    file_name = ""

    if len(sys.argv) <= 1:
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
