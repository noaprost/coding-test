import sys

n = int(sys.stdin.readline())

if 1 <= n < 10:
    exit(print(n))

nums = [0, 0, 9, 99, 999, 9999, 99999, 999999, 9999999]

l = len(str(n))

if n == 100000000:
    l -= 1
    n = l * (n - nums[l]) + 1
else:
    n = l * (n - nums[l])

digit = 1

for i in range(l - 1):
    n += 9 * digit * (1 + i)
    digit *= 10

print(n)