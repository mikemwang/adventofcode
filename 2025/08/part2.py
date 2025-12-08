import sys
import itertools

points = []

with open(sys.argv[1], "r") as f:
    points = [
        list(int(n) for n in line.rstrip().split(","))
        for line in f.readlines()
    ]

pairs = list(itertools.combinations(list(range(len(points))), 2))

def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 

pairs = sorted(pairs, key = lambda x : dist(points[x[0]], points[x[1]]))

circuits = []

for pair in pairs:
    a,b = pair

    a_circ = None
    b_circ = None
    for i, circuit in enumerate(circuits):
        if a in circuit:
            a_circ = i
        if b in circuit:
            b_circ = i
    if a_circ is None and b_circ is None:
        circuits.append({a, b})
    if a_circ == b_circ:
        continue
    elif a_circ is None:
        circuits[b_circ].add(a)
    elif b_circ is None:
        circuits[a_circ].add(b)
    else:
        circuits[a_circ] = circuits[a_circ].union(circuits[b_circ])
        circuits.pop(b_circ)

    if len(circuits) == 1 and len(circuits[0]) == len(points):
        # print(f"last 2 junction boxes: {points[a]} and {points[b]}")
        print(points[a][0] * points[b][0])
        break
