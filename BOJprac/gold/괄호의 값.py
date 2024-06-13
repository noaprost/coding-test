# 2504
import sys

bracket = sys.stdin.readline().rstrip()

s = input()
stack = []
ans = 0

for ss in s:
    if ss == "(":
        stack.append(ss)
    elif ss == "[":
        stack.append(ss)
    elif ss == ")":
        if len(stack) == 0:
            exit(print(0))
        else:
            tmp = stack.pop()
            if tmp == "(":
                continue
            else:
                exit(print(0))
    elif ss == "]":
        if len(stack) == 0:
            exit(print(0))
        else:
            tmp = stack.pop()
            if tmp == "[":
                continue
            else:
                exit(print(0))

if len(stack) != 0:
    exit(print(0))
else:
    exit(print(ans))