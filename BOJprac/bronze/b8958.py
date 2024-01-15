# OX퀴즈
import sys

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    total = 0
    sum = 0
    score = sys.stdin.readline().rstrip()
    memo = ""

    for i in range(len(score)):
        if score[i] == "O":
            if memo == score[i]:
                sum += 1
                total += sum
            else:
                sum = 1
                total += sum
            memo = "O"
        else:
            sum = 0
            memo = "X"
    print(total)
