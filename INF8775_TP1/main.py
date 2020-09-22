import sys


if __name__ == "__main__":

    file_name = ''

    if (len(sys.argv) <= 1):
        exit('Erreur: Pas assez d\'arguments. Vous devez indiquer le \
    nombre de points à générer et le nom du fichier de sortie.')

    if (len(sys.argv) > 2):
        exit('Erreur: Trop d\'arguments.')

    try:
        file_name = str(sys.argv[1])

        if file_name == "":
            raise ValueError()
    except:
        exit('Erreur: Le premier argument (nombre de points) doit être \
    un entier positif.')

    print(file_name)

    n = 0
    points = []

    with open(file_name, "r") as file:
        n = int(file.readline())

        for line in file:
            points.append(tuple(line.split()))

    print(points)
