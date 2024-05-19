# 2294
import sys

n, k = map(int, sys.stdin.readline().split())

nums = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] + [10001 for _ in range(k)]

for num in nums:
    for i in range(num, k + 1):
        dp[i] = min(dp[i], dp[i - num] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
