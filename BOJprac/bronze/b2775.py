import sys

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    dp = [[0 for _ in range(15)] for _ in range(15)]
    for i in range(1, 15):
        dp[0][i] = i

    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    # k층 n호에는 몇명이 살까?
    f = 1
    while f <= k:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[f][i] += dp[f - 1][j]
        f += 1

    print(dp[k][n])
