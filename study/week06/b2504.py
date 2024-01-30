# 괄호의 값
# 스택을 이용해서 괄호 짝 검사를 하고 거기에 맞게 계산도 하기
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
