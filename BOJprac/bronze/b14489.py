import sys

a, b = map(int, sys.stdin.readline().split())
twochick = int(sys.stdin.readline()) * 2

tong = a + b

if tong >= twochick:
    print(tong - twochick)
else:
    print(tong)
