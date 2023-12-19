# 9251
import sys

sys.setrecursionlimit(1001)

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

l1 = len(s1)
l2 = len(s2)

LCS = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

# LSC 값을 저장할 배열 만들기
for i in range(1, l1+1):
    for j in range(1, l2+1):
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
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
# for l in LCS:
#     print(l)
print(LCS[l1][l2])

# result = []
# i = l1 - 1
# j = l2 - 1
# while i != 0 and j != 0:
#     if LCS[i - 1][j] == LCS[i][j]:
#         i -= 1
#     elif LCS[i][j - 1] == LCS[i][j]:
#         j -= 1
#     else:
#         result.append(s1[j])
#         i -= 1
#         j -= 1

# for i in range(len(result) - 1, -1, -1):
#     print(result[i], end="")
