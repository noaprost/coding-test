# 수리공 항승
import sys
import math

n, length = map(int, sys.stdin.readline().split())
leak = list(map(int, sys.stdin.readline().split()))
leak.sort()

s = leak[0]
count = 1

for loc in leak[1:]:
    if loc in range(s, s + length):
        continue

    else:
        s = loc
        count += 1

print(count)
