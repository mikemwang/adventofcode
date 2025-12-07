import sys

with open(sys.argv[1], "r") as f:
    lines = [line.rstrip() for line in f.readlines()]

ans = 0

operations_per_q = lines[-1].split()
ans_per_q = [int(c) for c in lines[0].split()]

for i, line in enumerate(lines[1:-1]):
    i += 1
    for j, c in enumerate(line.split()):
        if operations_per_q[j] == "+":
            ans_per_q[j] += int(c)
        elif operations_per_q[j] == "*":
            ans_per_q[j] *= int(c)

print(sum(ans_per_q))


