# 분모 분자 각각 값 계산하고 두 수의 최대공약수로 분모 분자를 각각 나눠서 출력 해주면 될 듯

import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

nu = a * d + b * c
de = b * d

a1 = nu
b1 = de

while True:
    r = a1 % b1
    if r == 0:
        break
    else:
        a1 = b1
        b1 = r

print(int(nu / b1), int(de / b1))
