import sys

n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
idx = 0
calc = []
i = 1
while i < n + 1:
    if num[idx] >= i:
        while num[idx] >= i:
            stack.append(i)
            i += 1
            calc.append("+")
        if stack[-1] == num[idx]:
            stack.pop()
            calc.append("-")
            idx += 1
    elif num[idx] < i:
        if stack[-1] == num[idx]:
            stack.pop()
            calc.append("-")
            idx += 1
        else:
            exit(print("NO"))
while stack:
    if stack[-1] == num[idx]:
        stack.pop()
        calc.append("-")
        idx += 1
    else:
        exit(print("NO"))

for c in calc:
    print(c)
