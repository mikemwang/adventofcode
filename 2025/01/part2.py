import sys

def main(infile):
    with open(infile, "r") as f:
        rotations = f.readlines()
    ans = 0
    n = 50
    for rotation in rotations:
        # print(rotation[:-1])
        sign = 1 if rotation[0] == "R" else -1
        absval = int(rotation[1:])

        ans += (absval // 100)

        remainder = absval%100
        if remainder > 0:
            if 99 < n + sign*remainder or (n + sign*remainder < 1 and n > 0):
                ans += 1

        n = (n + sign*absval) % 100
        # print(n, ans)

    print(ans)

if __name__ == "__main__":
    infile = sys.argv[1]
    main(infile)
