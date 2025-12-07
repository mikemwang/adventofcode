import sys
import io
from functools import lru_cache

with open(sys.argv[1], "r") as f:
    LINES = [line.rstrip() for line in f.readlines()]

@lru_cache(maxsize=1024)
def ways_to_reach_end(line_num, col_num):
    if line_num == len(LINES) - 1:
        return 1
    c = LINES[line_num][col_num]
    if c == ".":
        return ways_to_reach_end(line_num+1, col_num)
    if c == "^":
        return ways_to_reach_end(line_num+1, col_num-1) + \
            ways_to_reach_end(line_num+1, col_num+1)

print(ways_to_reach_end(1, LINES[0].index("S")))

