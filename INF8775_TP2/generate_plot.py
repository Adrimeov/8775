from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
result_folder = "results"
result_files_names = ["mean_results_progdyn.txt",
                        "mean_results_tabou.txt",
                      "mean_results_vorace.txt"]

result_matrix = np.zeros((3, 7, 2))


for matrix_index, file in enumerate(result_files_names):
    with open(Path(result_folder, file), "r") as result:
        for line_index, line in enumerate(result.readlines()):
            parse_line = line.split("\t")
            parse_line[2] = parse_line[2].replace("\n","")
            parse_line = [float(x) for x in parse_line]
            parse_line = parse_line[1:]
            result_matrix[matrix_index, line_index, :] = parse_line


table_title_name = ["Temps d'éxécution moyen en seconde pour chaque "
                    "\nalgorithme selon la taille d'échantillon",
                    "Hauteur de tour moyenne pour chaque\nalgorithme selon la taille d'échantillon"]

# for i in range(2):
#     val1 = ["ProgDyn", "Tabou", "Vorace"]
#     val2 = ["100", "500", "1000", "5000", "10000", "50000", "100000"]
#     val3 = np.round(result_matrix[:, :, i].T, 5)
#
#     fig, ax = plt.subplots(figsize=(7,2))
#     ax.set_axis_off()
#     table = ax.table(
#         cellText=val3,
#         rowLabels=val2,
#         colLabels=val1,
#         rowColours=["palegreen"] * 10,
#         colColours=["palegreen"] * 10,
#         cellLoc='center',
#         loc='upper left')
#
#     ax.set_title(table_title_name[i],
#                  fontweight="bold")
#
#     plt.savefig("./figures/tableau_" + str(i) + ".png")


algo = ["dynamique", "tabou", "vorace"]
for i in range(3):
    #Test du rapport
    sample_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
    times = result_matrix[i, :, 0]

    slope, intercept, r_value, _, _ = linregress(np.log(sample_sizes), np.log(times))
    log_lin_values = np.exp([slope * np.log(n) + intercept for n in sample_sizes])

    axes = plt.subplot()
    axes.set(xlabel="Taille d'échantillon", ylabel="Temps d'éxécution (s)", title=f"Test de puissance pour l'algorithme {algo[i]}")
    axes.scatter(sample_sizes, times)
    axes.plot(sample_sizes, log_lin_values, color="r")
    axes.text(150, 1, "R-squared = {}".format(np.round(r_value, 4)))
    axes.grid()

    plt.xscale("log")
    plt.yscale("log")
    plt.xlim(min(sample_sizes), max(sample_sizes))
    plt.savefig(f"./figures/puissance_{algo[i]}")
    plt.clf()

    print("Regression R-Squared = " + str(r_value))




# for i in range(3)
#Test du rapport

algo = ["dynamique", "tabou", "vorace"]
lambdas = [
    lambda n: n ** 2.2,
    lambda n: n ** 1.3,
    lambda n: n**.87 * np.log(n)
]

for i in range(3):
    plt.xlim(100, 100000)
    sample_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
    times = result_matrix[i, :, 0]

    estimated_times = [lambdas[i](n) for n in sample_sizes]
    ratio_r = np.divide(times, estimated_times)

    axes = plt.subplot()
    axes.set(xlabel="Taille d'échantillon", ylabel="Temps d'éxécution", title=f"Test du rapport pour l'algorithme {algo[i]}")
    axes.plot(sample_sizes, ratio_r)
    axes.grid()

    plt.savefig(f"./figures/rapport_{algo[i]}")
    plt.clf()



algo = ["dynamique", "tabou", "vorace"]

for i in range(3):

    sample_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
    times = result_matrix[i, :, 0]
    estimated_times = [lambdas[i](n) for n in sample_sizes]

    slope, intercept, r_value, _, _ = linregress(estimated_times, times)
    axes = plt.subplot()
    axes.set(xlabel="Taille d'échantillon", ylabel="Temps d'éxécution", title=f"Test des constantes avec l'algorithme {algo[i]}")
    axes.scatter(estimated_times, times)
    axes.plot(estimated_times, [slope * n + intercept for n in estimated_times], color="r")
    axes.text(0.1, 2.5, "R-squared = {}".format(np.round(r_value, 4)))
    axes.grid()

    plt.savefig(f"./figures/constante_{algo[i]}")
    plt.clf()

    print("Regression R-Squared = " + str(r_value))

