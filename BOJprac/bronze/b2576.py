# 홀수
import sys

nums = [int(sys.stdin.readline()) for _ in range(7)]
odd = []
for n in nums:
    if n % 2 != 0:
        odd.append(n)

if len(odd) == 0:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))
