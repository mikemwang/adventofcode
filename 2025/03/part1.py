import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

ans = 0
for line in lines:
    line = line.rstrip()
    largest = 0
    for i, c in enumerate(line[:-1]):
        c = int(c)
        if c < largest // 10:
            continue
        for d in line[i+1:]:
            d = int(d)
            if 10*c + d > largest:
                largest = 10*c + d
    ans += largest

print(ans)
