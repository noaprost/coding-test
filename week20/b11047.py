# 동전 0
import sys

n, k = map(int, sys.stdin.readline().split())

value = [int(sys.stdin.readline()) for _ in range(n)]

ans = 0

for i in range(n - 1, -1, -1):
    if value[i] > k:
        continue
    else:
        remain = k % value[i]
        ans += k // value[i]
        k = remain
        if remain == 0:
            exit(print(ans))
