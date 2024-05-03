# 뉴비의 기준은 뭘까?
import sys

n, m = map(int, sys.stdin.readline().split())

if n >= m:
    if m == 1 or m == 2:
        print("NEWBIE!")
    else:
        print("OLDBIE!")
else:
    print("TLE!")
