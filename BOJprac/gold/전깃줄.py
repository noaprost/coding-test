# 2565
import sys

n = int(sys.stdin.readline())

elec = []
dp = [1 for _ in range(n)]

for _ in range(n):
    elec.append(list(map(int, sys.stdin.readline().split())))

elec.sort()

for i in range(n):  # 아래
    for j in range(i):  # 위
        if elec[i][1] > elec[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
