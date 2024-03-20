# 1107
import sys

n = int(sys.stdin.readline())
breakNum = int(sys.stdin.readline())
ans = abs(100 - n)

if breakNum != 0:
    breakBtns = list(sys.stdin.readline().split())
else:
    breakBtns = []

for i in range(1000000):
    isClickable = True
    for num in str(i):
        if num in breakBtns:
            isClickable = False
            break
    if isClickable:
        ans = min(ans, len(str(i)) + abs(i - n))

print(ans)
