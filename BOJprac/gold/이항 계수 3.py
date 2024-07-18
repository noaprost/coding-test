# 이항계수3
# 페르마의 소정리
import sys


def power(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (power(a, b // 2) ** 2 * a) % p
    else:
        return (power(a, b // 2) ** 2) % p


p = 1000000007
n, k = map(int, sys.stdin.readline().split())

facto = [1 for _ in range(n + 1)]

for i in range(2, n + 1):
    facto[i] = facto[i - 1] * i % p

a = facto[n]
b = (facto[n - k] * facto[k]) % p

print((a % p) * (power(b, p - 2) % p) % p)
