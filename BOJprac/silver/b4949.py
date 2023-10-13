# 괄호 짝 찾기 upgrade ver
# 달라진점 -> 괄호 종류 () []
#         -> 괄호가 하나도 없어도 균형이 잡혔다고 판단

import sys

while True:
    ps = sys.stdin.readline().rstrip()
    stack = []
    check = False

    # 종료조건
    if len(ps) == 1 and ps[0] == ".":
        break

    for i in range(len(ps)):
        if ps[i] == "(":
            stack.append(ps[i])

        elif ps[i] == "[":
            stack.append(ps[i])

        elif ps[i] == ")":
            if len(stack) == 0:
                print("no")
                check = True
                break

            if stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                check = True
                break
        elif ps[i] == "]":
            if len(stack) == 0:
                print("no")
                check = True
                break

            if stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                check = True
                break
        else:
            continue

    if not check:
        if len(stack) != 0:
            print("no")
        else:
            print("yes")
