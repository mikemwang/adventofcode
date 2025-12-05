import sys
with open(sys.argv[1], "r") as f:
    lines = f.readlines()

ranges = []
ingredient_ids = []

get_ranges = True
for line in lines:
    line = line.rstrip()
    if not line:
        get_ranges = False
        continue
    if get_ranges:
        a, b = line.split("-")
        ranges.append(tuple(sorted([int(a), int(b)])))
    else:
        ingredient_ids.append(int(line))

ans = 0
for iid in ingredient_ids:
    for a,b in ranges:
        if a <= iid <= b:
            ans += 1
            break
print(ans)
