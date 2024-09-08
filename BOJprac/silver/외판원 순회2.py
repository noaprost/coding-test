# 10971
import sys

INF = 1000000000
n = int(sys.stdin.readline())
w = []

for _ in range(n):
    w.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(2**n)] for _ in range(n)]


def tps(c, v):
    if v == (2**n) - 1 and w[c][0]:
        dp[c][v] = w[c][0]
        return w[c][0]
    if dp[c][v] == -1:
        return -1
    if dp[c][v]:
        return dp[c][v]
    m = INF
    for k in range(n):
        if not (1 << k) & v:
            if not w[c][k]:
                continue
            tmp = tps(k, (1 << k) | v)
            if tmp != -1 and m > tmp + w[c][k]:
                m = tmp + w[c][k]

    if m == INF:
        dp[c][v] = -1
        return -1
    else:
        dp[c][v] = m
        return dp[c][v]


print(tps(0, 1))
