# A+B-6
import sys

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    a, b = map(int, sys.stdin.readline().split(","))
    print(a + b)
