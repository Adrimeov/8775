import math

GRID_SIZE = 1000000

MAX_DIST =  math.sqrt(GRID_SIZE**2 + GRID_SIZE**2) # diagonale du carré de côté 1000000

'''
Calcule la distance entre deux points
'''
def distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)
