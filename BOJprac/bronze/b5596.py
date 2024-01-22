# 시험 점수
import sys

s1 = list(map(int, sys.stdin.readline().split()))
s2 = list(map(int, sys.stdin.readline().split()))

if sum(s1) > sum(s2):
    print(sum(s1))
else:
    print(sum(s2))
