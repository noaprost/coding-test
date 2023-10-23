import sys

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    padoban = [0, 1, 1, 1, 2, 2]
    n = int(sys.stdin.readline())
    if n < 6:
        print(padoban[n])
    else:
        for i in range(5, n + 1):
            padoban.append(padoban[i - 4] + padoban[i])
        print(padoban[n])
