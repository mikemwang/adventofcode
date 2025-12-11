import sys
from collections import deque

lights = []
buttons = []
joltages = []
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        line = line.rstrip()
        elements = line.split()
        lights.append(int("".join(["1" if x =="#" else "0" for x in elements[0][1:-1]])[::-1], base=2))
        buttons.append([
            sum(1 << int(n) for n in x[1:-1].split(",")) for x in elements[1:-1]
        ])
        joltages.append(list(int(x) for x in elements[-1][1:-1].split(",")))
    

ans = 0
for i in range(len(lights)):
    encountered_states = set()
    options = buttons[i]
    q = deque([(0, 0)])
    n = 0
    while True:
        state, n = q.popleft()
        encountered_states.add(state)
        if state == lights[i]:
            break
        for option in options:
            new_state = state ^ option
            if new_state in encountered_states:
                continue
            q.append((new_state, n+1))
    ans += n
print(ans)

