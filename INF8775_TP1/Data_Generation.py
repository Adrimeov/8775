import sys

from main import execute_closest_points
from gen import generate_samples


NB_REPETITIONS = 3
MAX_SAMPLES = 500000000
SAMPLES_FILE_NAME = "samples.txt"

nb_samples = 100
step = 100
sample_time_pairs = []


algo = None
algo_name = "brute"

# if len(sys.argv) <= 1:
#     exit('Erreur: Pas assez d\'arguments. Vous devez indiquer le '
#          'nombre de points à générer et le nom du fichier de sortie.')
#
# if len(sys.argv) > 2:
#     exit('Erreur: Trop d\'arguments.')
#
# try:
#     algo_name = str(sys.argv[1])
# except:
#     exit('Erreur: Le premier argument (nombre de points) doit être un entier positif.')


data_file_name = "generated_data_5millions" + algo_name + ".txt"

with open(data_file_name, "w") as file:
    file.write(algo_name + "\n")
    file.write(str(NB_REPETITIONS) + "\n")

    while nb_samples <= MAX_SAMPLES:

        average_time = 0

        for i in range(NB_REPETITIONS):
            # Generating new samples each iterations
            generate_samples(nb_samples, SAMPLES_FILE_NAME)
            average_time += execute_closest_points(SAMPLES_FILE_NAME, algo_name)

        average_time /= NB_REPETITIONS
        print(str(nb_samples) + " " + str(average_time))
        file.write(str(nb_samples) + " " + str(average_time) + "\n")

        nb_samples += step  # Increase sample size at the end

        if nb_samples / step == 10:
            step *= 10

