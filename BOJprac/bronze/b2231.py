import sys

n = int(sys.stdin.readline())

i = 1
sum = 0
creator = 0

while i <= 1000000:
    if int(i) >= n:
        print(0)
        break

    sum += i
    i = str(i)

    for ii in i:
        sum += int(ii)

    if sum == n:
        creator = int(i)
        print(creator)
        break

    i = int(i) + 1
    sum = 0
