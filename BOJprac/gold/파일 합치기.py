# 11066
import sys


testCase = int(sys.stdin.readline())

for _ in range(testCase):
    n = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            cost = 10000000000
            for k in range(j - i):
                cost = min(cost, dp[i][i + k] + dp[i + k + 1][j])
            dp[i][j] = cost + sum(files[i : j + 1])

    print(dp[0][n - 1])
