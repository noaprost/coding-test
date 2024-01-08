# 2023년은 무엇이 특별할까?
import sys

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    y = int(sys.stdin.readline())

    year = y + 1

    n = y % 100

    if(year % n == 0):
        print("Good")
    else:
        print("Bye")