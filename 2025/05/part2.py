import sys
with open(sys.argv[1], "r") as f:
    lines = f.readlines()

ranges = []

for line in lines:
    line = line.rstrip()
    if not line:
        break
    a, b = line.split("-")
    ranges.append(tuple(sorted([int(a), int(b)])))

ans = 0

ranges = sorted(ranges, key=lambda x: x[0])

combined_ranges = None

for a,b in ranges:
    if combined_ranges is None:
        combined_ranges = [(a,b)]
        continue
    if a <= combined_ranges[-1][-1]:
        if b > combined_ranges[-1][-1]:
            combined_ranges[-1] = (combined_ranges[-1][0], b)
    else:
        combined_ranges.append((a,b))

print(sum([b-a+1 for a,b in combined_ranges]))
