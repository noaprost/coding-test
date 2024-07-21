# 16565
import sys

n = int(sys.stdin.readline())
dp = [[0] * 53 for _ in range(53)]
dp[0][0] = dp[1][0] = dp[1][1] = 1

for i in range(2, 53):
    dp[i][0] = dp[i][i] = 1
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

ans = 0
type_num, flag = 1, 1

while n >= 4:
    ans += flag * dp[13][type_num] * dp[52 - type_num * 4][n - 4] % 10007
    type_num += 1
    flag *= -1
    n -= 4

print(ans % 10007)
