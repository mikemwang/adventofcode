import sys
import time

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

#   the largest n digit sequence must start with the largest number with
#   at least n-1 characters after it

def max_within_nums(i, nums, l, memo=None):
    if memo is None:
        memo = [[0 for _ in range(12+1)] for _ in range(len(nums))]
    if len(nums) < l:
        raise ValueError(f"len(nums) {len(nums)} is less than l {l}")

    if l == 1:
        memo[i][l] = max(nums)

    if memo[i][l] > 0:
        return memo[i][l]

    largest = 0
    target = max(nums[:-(l-1)])
    for j,n in enumerate(nums[:-(l-1)]):
        if n != target:
            continue
        x = n * 10**(l-1) + max_within_nums(j, nums[j+1:], l-1, memo)
        if x > largest:
            largest = x
    memo[i][l] = largest
    return largest

t = time.time()
print(sum(max_within_nums(0, [int(c) for c in line.rstrip()], 12) for line in lines))
print(f"{time.time()-t:.2f}")

