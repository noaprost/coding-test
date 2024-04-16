# 이칙 연산
import sys

a, b, c = map(int, sys.stdin.readline().split())

if (a / b) > (b / c):
    print(int((a / b) * c))
else:
    print(int((b / c) * a))
