import sys

with open(sys.argv[1], "r") as f:
    lines = [line[:-1] for line in f.readlines()]

state = 0

nums = []
operation = None
ans = 0

for i in range(len(lines[0])-1, -2, -1):
    if i == -1:
        state = 1
    if state == 0:
        if "".join(line[i] for line in lines) == " "*len(lines) and operation is not None:
            state = 1
        else:
            num = "".join(line[i] for line in lines[:-1])
            nums.append(int(num))
            if lines[-1][i] != " ":
                operation = lines[-1][i]
    if state == 1:
        if operation == "+":
            ans += sum(nums)
        elif operation == "*":
            product = 1
            for num in nums:
                product *= num
            ans += product
        nums = []
        operation = None
        state = 0

print(ans)
