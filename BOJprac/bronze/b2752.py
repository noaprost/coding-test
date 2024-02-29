# 세수정렬
import sys

num = list(map(int, sys.stdin.readline().split()))
num.sort()
print(*num)
