import sys

n = int(sys.stdin.readline())
stairs = [0]
for _ in range(n):
    s = int(sys.stdin.readline())
    stairs.append(s)

if n == 1:
    exit(print(stairs[1]))

dp = [[], [stairs[1], 0], [stairs[2], stairs[1] + stairs[2]]]

for i in range(3, n + 1):
    dp.append(
        [
            max(dp[i - 2][0], dp[i - 2][1]) + stairs[i],
            dp[i - 1][0] + stairs[i],
        ]
    )

print(max(dp[n][0], dp[n][1]))
