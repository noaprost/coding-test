# 직각 삼각형
import sys

num = list(map(int, sys.stdin.readline().split()))
num.sort()

while num[0] != 0:
    if pow(num[2], 2) == pow(num[0], 2) + pow(num[1], 2):
        print("right")
    else:
        print("wrong")

    num = list(map(int, sys.stdin.readline().split()))
    num.sort()
