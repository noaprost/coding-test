# 잃어버린 괄호

import sys

calc = sys.stdin.readline().rstrip()  # 식
ans = 0
num = ""
i = 0
while i < len(calc) and calc[i] != "-":
    if calc[i] != "+":
        num += calc[i]
    else:
        ans += int(num)
        num = ""
    i += 1
ans += int(num)
num = ""

while i < len(calc):
    tmp = 0
    num = ""
    while i < len(calc) and calc[i] != "-":
        if calc[i] != "+":
            num += calc[i]
        else:
            tmp += int(num)
            num = ""
        i += 1
    if num != "":
        tmp += int(num)
    ans -= tmp
    i += 1

print(ans)
