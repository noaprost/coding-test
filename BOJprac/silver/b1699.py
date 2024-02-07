# 제곱수의 합
import sys

n = int(sys.stdin.readline())

dp = [i for i in range(n + 1)]  # 우선은 전부 최대치인 1^2 항의 개수로 채워줌

for i in range(1, n + 1):
    for j in range(1, i):  # i보다는 작아야함
        jj = pow(j, 2)
        
        # 제곱수 자체가 i보다 커버리면 의미x
        if jj > i:
            break

        # 최소항으로 바꿔줘야 하므로
        if dp[i] > dp[i - jj] + 1:
            dp[i] = dp[i - jj] + 1

print(dp[n])
