import argparse
import sys
from glouton import Glouton


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
        blocks.append(Glouton.Bloc(sample[0], sample[1], sample[2]))

    return blocks


if __name__ == "__main__":
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

    samples = read_samples(parameters['path'])
    blocks = generate_blocks(samples)
