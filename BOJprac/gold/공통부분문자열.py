# 5582
import sys

sys.setrecursionlimit(4001)

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

l1 = len(s1)
l2 = len(s2)

LCS = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

# LSC 값을 저장할 배열 만들기
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if i == 0 or j == 0:
            if LCS[i - 1][j] == 1:
                LCS[i][j] = 1
            elif s1[i - 1] == s2[j - 1]:
                LCS[i][j] = 1
            else:
                LCS[i][j] = 0
        elif s1[i - 1] == s2[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = 0

m = 0
for L in LCS:
    if max(L) > m:
        m = max(L)

print(m)
