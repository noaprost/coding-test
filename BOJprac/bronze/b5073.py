# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우

import sys

a, b, c = map(int, sys.stdin.readline().split())

while a != 0:
    if max(a, b, c) == a:
        if a >= (b + c):
            print("Invalid")
            a, b, c = map(int, sys.stdin.readline().split())
            continue
    elif max(a, b, c) == b:
        if b >= (a + c):
            print("Invalid")
            a, b, c = map(int, sys.stdin.readline().split())
            continue
    elif max(a, b, c) == c:
        if c >= (a + b):
            print("Invalid")
            a, b, c = map(int, sys.stdin.readline().split())
            continue

    if len(set([a, b, c])) == 1:
        print("Equilateral")
    elif len(set([a, b, c])) == 2:
        print("Isosceles")
    elif len(set([a, b, c])) == 3:
        print("Scalene")

    a, b, c = map(int, sys.stdin.readline().split())
