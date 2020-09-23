import sys

from main import execute_closest_points
from gen import generate_samples


NB_REPETITIONS = 100
MAX_SAMPLES = 1000000
SAMPLES_FILE_NAME = "samples.txt"
DATA_FILE_NAME = "generated_data.txt"

nb_samples = 100
sample_time_pairs = []


algo = None
algo_name = ""

if len(sys.argv) <= 1:
    exit('Erreur: Pas assez d\'arguments. Vous devez indiquer le '
         'nombre de points à générer et le nom du fichier de sortie.')

if len(sys.argv) > 2:
    exit('Erreur: Trop d\'arguments.')

# TODO: selectionner l'argument Algo
try:
    algo_name = str(sys.argv[1])
    if algo_name == "brute_force":
        algo = execute_closest_points
    elif algo_name == "recursif":
        algo = execute_closest_points
    elif algo_name == "seuil":
        algo = execute_closest_points
    else:
        raise ValueError()
except:
    exit('Erreur: Le premier argument (nombre de points) doit être un entier positif.')

while nb_samples <= MAX_SAMPLES:

    for i in range(NB_REPETITIONS):
        average_time = 0
        generate_samples(nb_samples, SAMPLES_FILE_NAME)

        # TODO: call the right algo
        # average_time += execute_closest_points(FILE_NAME, ALGO)

    average_time /= NB_REPETITIONS
    # print(str(nb_samples)+ " " + str(average_time))
    sample_time_pairs.append((nb_samples, average_time))

    nb_samples *= 10  # Increase sample size at the end

with open(DATA_FILE_NAME, "w") as file:
    # TODO: get the algorithm
    file.write("NOM DE L\"ALGO")
    for sample_time_pair in sample_time_pairs:
        file.write(str(sample_time_pair[0]) + " " + str(sample_time_pair[1]))
