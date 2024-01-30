# 떡 먹는 호랑이
import sys

day, k = map(int, sys.stdin.readline().split())
sum = 0
a = 1
b = 1

while True:
    a1 = a
    b1 = b
    for i in range(2, day):
        sum = a1 + b1
        a1 = b1
        b1 = sum

    if sum == k:
        print(a)
        print(b)
        break

    if sum > k:
        a += 1
        b = 1

    b += 1
