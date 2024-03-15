# 9935
# 스택 문제였구나
import sys

s = sys.stdin.readline().rstrip()
bomb = list(sys.stdin.readline().rstrip())
stack = []
bomb_len = len(bomb)

for i in range(len(s)):
    stack.append(s[i])
    if len(stack) >= bomb_len and stack[-bomb_len:] == bomb:
        for _ in range(bomb_len):
            stack.pop()

if len(stack) != 0:
    print("".join(stack))
else:
    print("FRULA")
