# 크게 만들기
import sys

d, count = map(int, sys.stdin.readline().split())
finDight = d - count
n = sys.stdin.readline().rstrip()

stack = []
stack.append(n[0])
i = 1

while count != 0 and i < d:
    if len(stack) == 0:
        stack.append(n[i])
        i += 1
    if stack[-1] < n[i]:
        stack.pop()
        count -= 1
    else:
        stack.append(n[i])
        i += 1

for j in range(i, d, 1):
    stack.append(n[j])

print("".join(stack[:finDight]))
