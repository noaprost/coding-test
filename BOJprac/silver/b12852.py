# 1로 만들기 2
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

import sys

n = int(sys.stdin.readline())

dp = [0, 0, 1, 1]

if n >= 4:
    for i in range(4, n + 1):
        val1 = dp[i - 1] + 1
        val2 = dp[i - 1] + 1
        val3 = dp[i - 1] + 1

        if i % 3 == 0:
            val1 = dp[i // 3] + 1
        if i % 2 == 0:
            val2 = dp[i // 2] + 1

        dp.append(min(val1, val2, val3))

print(dp[n])
