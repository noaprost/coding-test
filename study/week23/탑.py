# 2493
import sys

n = int(sys.stdin.readline())

top = list(map(int, sys.stdin.readline().split()))

ans = []

stack = []
num = 1

for t in top:
    while len(stack) != 0 and stack[-1][0] < t:
        stack.pop()
    stack.append([t, num])
    if len(stack) > 1:
        ans.append(stack[-2][1])
    else:
        ans.append(0)
    num += 1

for a in ans:
    print(a, end=" ")
