import argparse
import sys
import time

from os import listdir
from os.path import isfile, join
from customLib import CustomLib


def generate_data(algo):
    algo_dictionary = {"vorace": CustomLib.algo_glouton,
                       "progdyn": CustomLib.algo_dynamic,
                       "tabou": CustomLib.algo_tabu}
    data_dir = "./data/"

    files = [f for f in listdir(data_dir) if isfile(join(data_dir, f))]
    sample_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]

    for sample_size in sample_sizes:
        target_files_name = f"b{sample_size}_"
        target_files = [file for file in files if target_files_name in file]

        mean_time = 0
        mean_height = 0

        for target_file in target_files:
            samples = read_samples(join(data_dir, f"{target_file}"))
            blocs = generate_blocks(samples)

            start = time.time()
            hauteur, tower = algo_dictionary[algo](blocs)
            total_time = time.time() - start

            mean_time += total_time
            mean_height += hauteur

        mean_time = mean_time / len(target_files)
        mean_height = mean_height / len(target_files)

        with open(join("./results", f"mean_results_{algo}.txt"), "a") as f:
            f.write(f"{sample_size}\t{mean_time}\t{mean_height}\n")


def read_samples(filepath):
    blocks = []

    with open(filepath, 'r') as file:
        for line in file:
            blocks.append(tuple(int(a) for a in line.split()))

    return blocks


def generate_blocks(samples):
    samples.sort(key=lambda tup: ((tup[1] * tup[2]) * (tup[1] / tup[2])), reverse=True)
    blocks = []

    for sample in samples:
        blocks.append(CustomLib.Bloc(sample[0], sample[1], sample[2]))

    return blocks


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        exit('Erreur: Pas assez d\'arguments.')

    arguments = ["--algo"]
    parser = argparse.ArgumentParser()

    for argument in arguments:
        parser.add_argument(argument)

    args = parser.parse_args()
    args_as_dict = vars(args)
    parameters = {a: vars(args)[a] for a in vars(args) if vars(args)[a] != ""}

    generate_data(**parameters)
