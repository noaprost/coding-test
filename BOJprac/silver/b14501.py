# 퇴사
import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
t = [0] * (n + 1)
p = [0] * (n + 1)
for i in range(1, n + 1):
    t[i], p[i] = map(int, sys.stdin.readline().split())

for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], dp[i])
    finDate = i + t[i] - 1
    if finDate <= n:
        dp[finDate] = max(dp[finDate], dp[i - 1] + p[i])

print(dp[n])
