# 1918
import sys


def prec(ch):
    if ch == "(" or ch == ")":
        return 0
    elif ch == "+" or ch == "-":
        return 1
    elif ch == "*" or ch == "/":
        return 2


expr = sys.stdin.readline().rstrip()
stack = []
i = 0
while i < len(expr):
    ch = expr[i]
    if ch == "+" or ch == "-" or ch == "*" or ch == "/":
        while len(stack) != 0 and (prec(ch) <= prec(stack[-1])):
            print(stack.pop(), end="")
        stack.append(ch)
    elif ch == "(":
        stack.append("(")
    elif ch == ")":
        t = stack.pop()
        while t != "(":
            print(t, end="")
            t = stack.pop()
    else:
        print(ch, end="")
    i += 1

while len(stack) != 0:
    print(stack.pop(), end="")
