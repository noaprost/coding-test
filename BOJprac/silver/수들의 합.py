import sys

s = int(sys.stdin.readline())
if s == 1:
    exit(print(1))
sum = 0
i = 1
while sum <= s:
    sum = (i * (i + 1)) // 2
    i += 1

print(i - 2)
