import time
from utils import MAX_DIST, distance

'''
Algorithme Force Brute
Si le nombre de points est suffisamment petit, on préfère utiliser cet algorithme.
'''
def brute_force(points):
    dist_min = MAX_DIST
    for pos, pt1 in enumerate(points):
        for pt2 in points[(pos+1):]:
            tmp_dist = distance(pt1, pt2)
            dist_min = min(tmp_dist, dist_min)
    return dist_min


def execute_brute_force(points):
    start = time.time()
    min_brute_force = brute_force(points)
    end = time.time()
    # print("BF: ", min_brute_force)
    return end-start
