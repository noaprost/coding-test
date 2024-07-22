# 15824
import sys


def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a

    tmp = pow(a, b // 2)

    if b % 2 == 0:
        return tmp * tmp % 1000000007
    else:
        return tmp * tmp * a % 1000000007


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

ans = 0
for i in range(n):
    ans += nums[i] * (pow(2, i) - pow(2, n - i - 1))

print(ans % 1000000007)
