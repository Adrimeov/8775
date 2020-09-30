import sys

from main import execute_closest_points
from gen import generate_samples


NB_REPETITIONS = 10
MAX_SAMPLES = 100000
SAMPLES_FILE_NAME = "samples.txt"

nb_samples = 100
sample_time_pairs = []


algo = None
algo_name = ""

if len(sys.argv) <= 1:
    exit('Erreur: Pas assez d\'arguments. Vous devez indiquer le '
         'nombre de points à générer et le nom du fichier de sortie.')

if len(sys.argv) > 2:
    exit('Erreur: Trop d\'arguments.')

try:
    algo_name = str(sys.argv[1])
    if algo_name == "brute":
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
    generate_samples(nb_samples, SAMPLES_FILE_NAME)

    for i in range(NB_REPETITIONS):
        average_time = 0
        average_time += execute_closest_points(SAMPLES_FILE_NAME, algo_name)

    average_time /= NB_REPETITIONS
    print(str(nb_samples) + " " + str(average_time))
    sample_time_pairs.append((nb_samples, average_time))

    nb_samples *= 10  # Increase sample size at the end

data_file_name = "generated_data_" + algo_name + ".txt"

with open(data_file_name, "w") as file:
    file.write(algo_name)
    for sample_time_pair in sample_time_pairs:
        file.write(str(sample_time_pair[0]) + " " + str(sample_time_pair[1]) + "\n")
