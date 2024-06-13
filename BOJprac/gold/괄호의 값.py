# 2504
import sys

bracket = list(sys.stdin.readline().rstrip())
stack = []
ans = 0
tmp = 1

for i in range(len(bracket)):
    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            exit(print(0))

        if bracket[i - 1] == "(":
            ans += tmp

        stack.pop()
        tmp //= 2

    elif bracket[i] == "]":
        if not stack or stack[-1] == "(":
            exit(print(0))

        if bracket[i - 1] == "[":
            ans += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(ans)
