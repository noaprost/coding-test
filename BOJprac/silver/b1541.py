# 잃어버린 괄호

import sys

calc = sys.stdin.readline().rstrip()  # 식
num = ""
plus = False
minus = False
ans = 0
tmp = 0
for c in calc:
    # c가 숫자이면
    if c != "+" and c != "-":
        num += c
    elif c == "-":
        if not plus and not minus:
            ans = int(num)
            num = ""
        elif not minus:
            ans -= tmp
            num = ""
    elif c == "+":
        if not plus and not minus:
            ans = int(num)
            num = ""
        elif not plus:
            tmp += int(num)
            num = ""
