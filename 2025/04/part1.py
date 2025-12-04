import sys
with open(sys.argv[1], "r") as f:
    rows = [l.rstrip() for l in f.readlines()]

ans = 0

row_limit = len(rows) 
col_limit = len(rows[0])

for i, row in enumerate(rows):
    for j, char in enumerate(row):
        if char != "@":
            continue
        neighbours = 0
        for a in range(-1, 2):
            for b in range(-1, 2):
                test_row = i + a
                test_col = j + b
                if (
                    test_row >= row_limit or\
                    test_row < 0 or\
                    test_col >= col_limit or\
                    test_col < 0
                ):
                    continue
                if test_row == i and test_col == j:
                    continue
                neighbours += rows[test_row][test_col] == "@"
        if neighbours < 4:
            ans += 1
print(ans)

