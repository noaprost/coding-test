# 10799
import sys

stack = []

bracket = sys.stdin.readline().rstrip()

count = 0

i = 0

tmp = 0

while i < len(bracket):
    if bracket[i] == "(" and bracket[i + 1] == ")":
        i += 1
        continue
    elif bracket[i] == "(" and bracket[i + 1] == "(":
        tmp += 1
        count += 1
    elif bracket[i] == ")" and bracket[i - 1] == "(":
        count += tmp
    elif bracket[i] == ")" and bracket[i - 1] == ")":
        tmp -= 1
    i += 1

print(count)
