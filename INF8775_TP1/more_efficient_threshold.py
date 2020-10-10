import sys

from main import execute_closest_points
from gen import generate_samples


NB_REPETITIONS = 3
MAX_SAMPLES = 1000
SAMPLES_FILE_NAME = "samples.txt"

nb_samples = 2
step = 1
sample_time_pairs = []


algo = None
algo_name = "recursif"


data_file_name = "recursif_under_1000" + algo_name + ".txt"

seuil = []
temps_tot = []

for k in range(1, 500, 5):
    seuil.append(k)
    average_time = 0

    for i in range(NB_REPETITIONS):
        # Generating new samples each iterations
        generate_samples(10000, SAMPLES_FILE_NAME)
        average_time += execute_closest_points(SAMPLES_FILE_NAME, algo_name, recursion=k)
    print("seuil: " + str(k) + " somme: " + str(average_time/NB_REPETITIONS))

    temps_tot.append(average_time)


import matplotlib.pyplot as plt
axes = plt.subplot()
axes.set(xlabel="seuil choisi", ylabel="time", title="Effet du seuil sur le temps de calcul pour n=10000")
axes.plot(seuil, temps_tot)
axes.grid()
plt.show()

