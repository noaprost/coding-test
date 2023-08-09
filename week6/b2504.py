# 괄호의 값
# 스택을 이용해서 괄호 짝 검사를 하고 거기에 맞게 계산도 하기
def barcketCheck(s):
    for ss in s:
        if ss == "(" or ss == "[":
            stack.append(ss)
        elif ss == ")" or ss == "]":
            if len(stack) == 0:
                return False
            else:
                tmp = stack.pop()
                if (tmp == "(" and ss == ")") or (tmp == "[" and ss == "]"):
                    continue
                else:
                    return False

    if len(stack) != 0:
        return False
    else:
        return True


s = input()
stack = []

print(barcketCheck(s))
