# 후위 표기식 2
import sys

n = int(sys.stdin.readline())
expr = sys.stdin.readline().rstrip()
nums = [float(sys.stdin.readline()) for _ in range(n)]

stack = []

for i in range(len(expr)):
    if expr[i] == "+":
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif expr[i] == "-":
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif expr[i] == "*":
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif expr[i] == "/":
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)
    else:
        stack.append(nums[ord(expr[i]) - 65])

print(f"{stack.pop():.2f}")