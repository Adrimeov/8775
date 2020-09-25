################################################################################
#
# Générateur d'exemplaires
#
# Ce script génère un exemplaire au hasard d'une taille de votre choix. Vous
# devez préciser le nombre de points que vous voulez générer ainsi que le nom du
# fichier de sortie.
#
# Input 1 (int): Nombre de points
# Input 2 (string): Nom du fichier de sortie
#
# Exemple d'utilisation à partir du terminal:
#
#     python3 gen.py 1000 ex1000.txt
#
# Dans cet exemple, une instance de 1000 points sera générée et sauvegardée dans
# le fichier ex1000.txt. Les coordonnées des points x et y seront dans
# l'intervalle [0, 1000000].
#
# Vous pouvez automatiser la génération de séries d'exemplaires à partir du
# terminal avec des commandes simples. Par exemple:
#
#     for x in {1..10}; do python3 gen.py 1000 1000-$x.txt; done
#
# Cette commande va générer 10 exemplaires de 1000 points, dans des fichiers
# nommés 1000-1.txt, 1000-2.txt, ..., 1000-10.txt
# 
################################################################################

import random
import sys

n = -1
fn = ''

if (len(sys.argv) <= 2):
    exit('Erreur: Pas assez d\'arguments. Vous devez indiquer le \
nombre de points à générer et le nom du fichier de sortie.')

if (len(sys.argv) > 3):
    exit('Erreur: Trop d\'arguments.')

try:
    n = int(sys.argv[1])
    if (n <= 0):
        raise ValueError()
except:
    exit('Erreur: Le premier argument (nombre de points) doit être \
un entier positif.')

fn = sys.argv[2]
c = 1000000
points = [[random.randint(0, c), random.randint(0, c)] for _ in range(n)]

with open(fn, 'w') as f:
    f.write(str(n) + '\n')
    for i in range(n):
        f.write(str(points[i][0]) + ' ' + str(points[i][1]) + '\n')
f.close()
