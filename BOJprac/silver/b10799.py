# 쇠막대기
import sys

stack = []

bracket = sys.stdin.readline().rstrip()

count = 0

i = 0

tmp = 0

while i < len(bracket):
    if bracket[i] == "(" and bracket[i + 1] == ")":
        count += tmp
        i += 1
    elif bracket[i] == "(":
        tmp += 1
    elif bracket[i] == ")":
        count += tmp
        tmp -= 1
    i += 1

print(count)
