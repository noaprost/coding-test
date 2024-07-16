# 1725
import sys

n = int(sys.stdin.readline())
q = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
max_res = 0

for i, h in enumerate(q):

    if stack and stack[-1][1] > h:
        while stack:
            _, s_h = stack.pop()
            w = 1
            if stack:
                w = stack[-1][0] + 1
            res = (i + 1 - w) * s_h
            max_res = max(res, max_res)
            if not stack or stack[-1][1] <= h:
                break

    if not stack or stack[-1][1] <= h:
        stack.append((i + 1, h))

while stack:
    _, s_h = stack.pop()
    w = 1
    if stack:
        w = stack[-1][0] + 1
    res = (n + 1 - w) * s_h
    max_res = max(res, max_res)

print(max_res)
