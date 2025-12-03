import sys

def get_n_digits(n):
    digits = 0
    while n > 10**digits:
        digits += 1
    return digits

with open(sys.argv[1], "r") as f:
    ranges = f.read()

ranges = ranges.split(",")

ans = 0

for r in ranges:
    start, end = r.split("-")
    start = int(start)
    end = int(end)
    for i in range(start, end+1):
        n_digits = get_n_digits(i)
        if n_digits % 2 > 0:
            continue
        if i // 10**(n_digits//2) == i % 10**(n_digits//2):
            ans += i

print(ans)

# an odd-digit number is always valid

# 1 digit: none
# 2 digit: 11,22,33,...,88,99
# 3 digit: none (?)
# 4 digit: 1010, 1111, 2020, 2121, 2222,
# [1-9][0-9]...[0-9] 


