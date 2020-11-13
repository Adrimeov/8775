from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
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

for i in range(2):
    val1 = ["ProgDyn", "Tabou", "Vorace"]
    val2 = ["100", "500", "1000", "5000", "10000", "50000", "100000"]
    val3 = np.round(result_matrix[:, :, i].T, 5)


    fig, ax = plt.subplots(figsize=(7,2))
    ax.set_axis_off()
    table = ax.table(
        cellText=val3,
        rowLabels=val2,
        colLabels=val1,
        rowColours=["palegreen"] * 10,
        colColours=["palegreen"] * 10,
        cellLoc='center',
        loc='upper left')

    ax.set_title(table_title_name[i],
                 fontweight="bold")

    plt.show()