# 사장님 도박은 재미로 하셔야 합니다
import sys

s = int(sys.stdin.readline())
sum = 0

while s != -1:
    sum += s
    s = int(sys.stdin.readline())

print(sum)
