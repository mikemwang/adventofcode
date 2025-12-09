import sys
import itertools
import math

with open(sys.argv[1], "r") as f:
    points = [[int(n) for n in line.split(",")] for line in f.readlines()]

combos = itertools.combinations(list(range(len(points))), 2)

def area(a, b):
    return (math.fabs((a[0]-b[0]))+1)*(math.fabs(a[1]-b[1])+1)

max_area = 0

for combo in combos:
    max_area = max(area(points[combo[0]], points[combo[1]]), max_area)

print(max_area)
