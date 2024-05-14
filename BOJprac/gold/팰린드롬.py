# 10942
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for s in range(n - i):
        e = s + i
        if s == e:
            dp[s][e] = 1
        elif num[s] == num[e]:
            if s + 1 == e:
                dp[s][e] = 1
            elif dp[s + 1][e - 1] == 1:
                dp[s][e] = 1

m = int(sys.stdin.readline())
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    if dp[start - 1][end - 1] == 1:
        print(1)
    else:
        print(0)
