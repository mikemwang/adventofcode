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
        if n_digits < 2: 
            continue
        i = str(i)
        for substr_len in range(1,n_digits//2+1):
            found = True
            substr = i[:substr_len]
            for j in range(0, len(i), substr_len):
                if i[j:min(j+substr_len, len(i))] != substr:
                    found = False
                    break
            if found:
                ans += int(i)
                break

print(ans)

# an odd-digit number is always valid

# 1 digit: none
# 2 digit: 11,22,33,...,88,99
# 3 digit: none (?)
# 4 digit: 1010, 1111, 2020, 2121, 2222,
# [1-9][0-9]...[0-9] 


