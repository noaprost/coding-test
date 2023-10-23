# 단어 뒤집기

import sys

s = sys.stdin.readline().strip()

ans = ""
stack = []
idx = 0

# 문자열 앞부터 하나씩 탐색
while idx < len(s):
    if s[idx] == " ":  # 공백이 나오면
        while len(stack) != 0:  # 스택이 빌때까지 꺼내줌
            st = stack.pop()
            ans += st
        ans += s[idx]  # 공백을 더해줌
        idx += 1
    elif s[idx] == "<":  # 여는 괄호가 나오면
        while len(stack) != 0:  # 우선 그전 단어들을 스택이 빌때까지 꺼내줌
            st = stack.pop()
            ans += st
        while s[idx] != ">":  # 그리고 닫는 괄호가 나올때까지 넘겨줌
            ans += s[idx]
            idx += 1
        ans += s[idx]
        idx += 1
    else:
        stack.append(s[idx])  # 공백이나 괄호가 아니면 단어, 스택에 넣어줌
        idx += 1

if len(stack) != 0:  # 마지막에 스택이 비어있지 않으면
    while len(stack) != 0:  # 남은 단어를 마저 꺼내줌
        st = stack.pop()
        ans += st
print(ans)
