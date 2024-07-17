# 3015
import sys

n = int(sys.stdin.readline())
people = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
ans = 0

for peo in people:
    while stack and stack[-1][0] < peo:
        ans += stack.pop()[1]

    if not stack:
        stack.append((peo, 1))
        continue

    if stack[-1][0] == peo:
        c = stack.pop()[1]
        ans += c

        if stack:
            ans += 1

        stack.append((peo, c + 1))

    else:
        stack.append((peo, 1))
        ans += 1

print(ans)
