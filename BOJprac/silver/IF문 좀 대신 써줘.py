# 19637
import sys

n, m = map(int, sys.stdin.readline().split())
power_sys = []

for _ in range(n):
    name, power = sys.stdin.readline().split()
    power_sys.append((int(power), name))

characters = [int(sys.stdin.readline()) for _ in range(m)]

for ch in characters:
    left = 0
    right = n
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if power_sys[mid][0] >= ch:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(power_sys[ans][1])
