import sys
import io

with open(sys.argv[1], "r") as f:
    lines = [line.rstrip() for line in f.readlines()]

beam_locs = set()
ans = 0
for line in lines:
    for i,c in enumerate(line):
        if c == "S":
            beam_locs.add(i)
        if c == "." and i in beam_locs:
            pass
        if c == "^" and i in beam_locs:
            beam_locs.remove(i)
            beam_locs.add(i+1)
            beam_locs.add(i-1)
            ans += 1
print(ans)
