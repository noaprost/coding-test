# 단어 뒤집기
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    stack = []
    ans = ""
    for ss in s:
        if ss == " ":
            while stack:
                ans += stack.pop()
            ans += " "
        else:
            stack.append(ss)
    while stack:
        ans += stack.pop()
    print(ans)
