# 몇개고?
import sys

time, drink = map(int, sys.stdin.readline().split())

if drink == 1 or time > 16 or time < 12:
    print(280)
elif drink == 0 and 12 <= time <= 16:
    print(320)
