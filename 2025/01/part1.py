def main():
    with open("input", "r") as f:
        rotations = f.readlines()
    n = 50
    ans = 0
    for rotation in rotations:
        sign = 1 if rotation[0] == "R" else -1
        val = int(rotation[1:])
        n = (n + sign*val) % 100
        if n == 0:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
