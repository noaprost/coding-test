# 1038
import sys

target = int(sys.stdin.readline())
n = 0
count = -1

if target <= 10:
    exit(print(target))

while n <= 9876543210:
    sn = str(n)
    isDec = True
    for i in range(len(sn) - 1):
        if int(sn[i]) <= int(sn[i + 1]):
            isDec = False
            break
    if isDec:
        count += 1

    if count == target:
        exit(print(int(n)))

    n = int(n) + 1

print(-1)
