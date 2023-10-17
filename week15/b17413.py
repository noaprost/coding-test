# 단어 뒤집기

import sys

s = sys.stdin.readline().strip()

ans = ""
stack = []
idx = 0

while idx < len(s):
    if s[idx] == " ":
        while len(stack) != 0:
            st = stack.pop()
            ans += st
        ans += s[idx]
        idx += 1
    elif s[idx] == "<":
        while len(stack) != 0:
            st = stack.pop()
            ans += st
        while s[idx] != ">":
            ans += s[idx]
            idx += 1
        ans += s[idx]
        idx += 1
    else:
        stack.append(s[idx])
        idx += 1

if len(stack) != 0:
    while len(stack) != 0:
        st = stack.pop()
        ans += st
print(ans)
