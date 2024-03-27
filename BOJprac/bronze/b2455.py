# 지능형 기차
import sys

count = []

total = 0

for _ in range(4):
    outPerson, inPerson = map(int, sys.stdin.readline().split())

    total += inPerson - outPerson

    count.append(total)

print(max(count))
