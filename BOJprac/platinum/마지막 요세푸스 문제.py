# 1179
import sys

n, k = map(int, sys.stdin.readline().split())
ans = 0
nn = 1
if k == 1:
    print(n)
else:
    while True:
        x = (nn - ans - 1) // (k - 1) + 1
        if nn + x > n:
            ans += (n - nn) * k
            break
        ans = (ans + k * x) % (nn + x)
        nn += x
    print(ans + 1)

# sys.setrecursionlimit(10**9)


# def Josephus(n, k):
#     if n == 1:
#         return 0
#     if k == 1:
#         return n - 1
#     if k <= n:
#         n2 = n - n / k
#         tmp = Josephus(n2, k) - n % k
#         if tmp < 0:
#             tmp += n2
#         return (k * (tmp % n2)) / (k - 1)
#     else:
#         return (Josephus(n - 1, k) + k) % n


# n, k = map(int, sys.stdin.readline().split())
# print(Josephus(n, k) + 1)
