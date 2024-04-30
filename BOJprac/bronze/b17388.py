# 와글와글 숭고한
import sys

num = list(map(int, sys.stdin.readline().split()))

if sum(num) >= 100:
    print("OK")
else:
    if min(num) == num[0]:
        print("Soongsil")
    elif min(num) == num[1]:
        print("Korea")
    elif min(num) == num[2]:
        print("Hanyang")
