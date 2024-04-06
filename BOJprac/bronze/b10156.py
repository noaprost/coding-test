# 과자
import sys

snack, n, money = map(int, sys.stdin.readline().split())

if snack * n <= money:
    print(0)
else:
    print(snack * n - money)
