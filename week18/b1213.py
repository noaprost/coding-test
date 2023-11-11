# 팰린드롬 만들기
# idea : 개수를 세서 짝수개면 남기고, 홀수개인건 사전순으로 가장 앞선것 딱 한개만 남기기
# 홀수개인 것이 2개 이상이면 바로 미안해 출력
# 홀수개인 것이 1개면 짝수개인 것들 중 사전순으로 앞선 것을 먼저 배치하고, 홀수개인 것을 가운데로 배치
# 근데 홀수개의 숫자가 3이상이면 또 짝수개들과 알파벳 순을 비교해서 1개만 남기고 양옆으로 배치하는 것도 중요

import sys

s = sys.stdin.readline().rstrip()

sLen = len(s)
sList = []
ans = [" " for _ in range(sLen)]
isOdd = False

for i in range(sLen):
    sList.append(s[i])

sList.sort()
print(sList)
for i in range(sLen):
    if i == 0:
        tmp = sList[i]
        tmpCnt = 1
    else:
        if tmp == sList[i]:
            tmpCnt += 1
            if tmpCnt % 2 == 0:
                ans[i - 1] = tmp
                ans[-i] = tmp
        else:
            if tmpCnt % 2 != 0:
                if isOdd:
                    exit(print("I'm Sorry Hansoo"))
                isOdd = True
                if sLen % 2 == 0:
                    exit(print("I'm Sorry Hansoo"))
                else:
                    ans[(sLen - 1) // 2] = tmp
                    tmp = sList[i]
                    tmpCnt = 1
            else:
                if tmpCnt % 2 == 0:
                    tmp = sList[i]
                    tmpCnt = 1
                    ans[i - 1] = tmp
                    ans[-i] = tmp

print(ans)
