# 1105
import sys

a, b = map(str, sys.stdin.readline().split())
count = 0

if len(a) != len(b):
    print(0)

else:
    for i in range(len(a)):
        if a[i] == b[i]:
            if a[i] == "8":
                count += 1
        else:
            break
    print(count)
