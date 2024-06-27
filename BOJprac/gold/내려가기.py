# 2096
import sys

n = int(sys.stdin.readline())
maps = list(map(int, sys.stdin.readline().split()))
max_dp = [maps[0], maps[1], maps[2]]
min_dp = [maps[0], maps[1], maps[2]]

for _ in range(n - 1):
    maps = list(map(int, sys.stdin.readline().split()))
    max_dp = [
        maps[0] + max(max_dp[0], max_dp[1]),
        maps[1] + max(max_dp),
        maps[2] + max(max_dp[1], max_dp[2]),
    ]
    min_dp = [
        maps[0] + min(min_dp[0], min_dp[1]),
        maps[1] + min(min_dp),
        maps[2] + min(min_dp[1], min_dp[2]),
    ]

print(max(max_dp), min(min_dp))
