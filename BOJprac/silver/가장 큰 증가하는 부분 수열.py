import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]
dp[0] = num[0]

i = 1
while i < n:
    tmp = 0
    for j in range(i):
        if tmp < dp[j] and num[j] < num[i]:
            tmp = dp[j]
    dp[i] = tmp + num[i]
    i += 1

print(max(dp))
