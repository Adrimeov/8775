import argparse
import sys
from customLib import CustomLib
import time


def algo_dynamic(blocks):
    blocks_ = sort_blocks(blocks)
    return CustomLib.algo_dynamic(blocks_)


def algo_glouton(blocks):
    blocks_ = sort_blocks(blocks)
    return CustomLib.algo_glouton(blocks_)


def construct_tower(path=None, algo="vorace", timer=False, solution=False):
    # tp.sh -a [vorace | progdyn | tabou] -e [path_vers_exemplaire]
    algo_dictionary = {"vorace": algo_glouton,
                       "progdyn": algo_dynamic,
                       "tabou": CustomLib.algo_tabu}

    samples = read_samples(parameters['path'])
    blocks = generate_blocks(samples)

    start = time.time()
    hauteur, tower = algo_dictionary[algo](blocks)
    end = time.time()
    total_time = (end - start) * 1000

    if bool(timer):
        print("Time to compute: " + str(total_time) + "ms")

    if solution:
        for bloc in tower:
            print(f"{bloc.getH()}, {bloc.getL()}, {bloc.getP()}")
    return hauteur


def read_samples(filepath):

    blocks = []

    with open(filepath, 'r') as file:
        for line in file:
            blocks.append(tuple(int(a) for a in line.split()))

    return blocks


def sort_blocks(blocks):
    blocks.sort(key=lambda block: (block.getL() * block.getP()), reverse=True)
    return blocks


def generate_blocks(samples):
    blocks = []

    for sample in samples:
        blocks.append(CustomLib.Bloc(sample[0], sample[1], sample[2]))

    return blocks


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        exit('Erreur: Pas assez d\'arguments.')

    arguments = ["--path", "--timer", "--algo", "--solution"]
    parser = argparse.ArgumentParser()

    for argument in arguments:
        parser.add_argument(argument)

    args = parser.parse_args()
    args_as_dict = vars(args)
    parameters = {a: vars(args)[a] for a in vars(args) if vars(args)[a] != ""}
    height = construct_tower(**parameters)



