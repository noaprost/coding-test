# 괄호 짝 찾기

# 규칙
# ( 는 스택에 push 한다
# ) 가 나오면 스택에서 pop 한다 -> 이때 꺼낼 (가 더이상 없으면 짝이 안맞는거
# 전부 끝난후 스택에 값이 남아있으면 짝이 안맞는거

import sys

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    check = False
    stack = []
    ps = sys.stdin.readline().strip()

    for i in range(len(ps)):
        if ps[i] == "(":
            stack.append(ps[i])
        elif ps[i] == ")":
            if len(stack) == 0:
                print("NO")
                check = True
                break
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    print("NO")
                    check = True
                    break
    if not check:
        if len(stack) != 0:
            print("NO")
        else:
            print("YES")
