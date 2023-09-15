import sys

n = int(sys.stdin.readline())

nums = map(int, sys.stdin.readline().split())

isPrime = True
count = 0

for num in nums:
    if num == 1:
        continue
    for j in range(2, num):
        if num % j == 0:
            isPrime = False
            break
    if isPrime:
        count += 1
    isPrime = True

print(count)
