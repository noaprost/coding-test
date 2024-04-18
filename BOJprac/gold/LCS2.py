# 9252
import sys

sys.setrecursionlimit(1001)

s1 = [" "] + list(sys.stdin.readline().rstrip())
s2 = [" "] + list(sys.stdin.readline().rstrip())

l1 = len(s1)
l2 = len(s2)

LCS = [[0 for _ in range(l2)] for _ in range(l1)]

for i in range(1, l1):
    for j in range(1, l2):
        if s1[i] == s2[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

leng = LCS[-1][-1]
print(leng)

result = []
i = l1 - 1
j = l2 - 1
while i > 0 and j > 0:
    if s1[i] == s2[j]:
        result.append(s1[i])
        if len(result) == leng:
            for i in range(len(result) - 1, -1, -1):
                print(result[i], end="")
            break
        i -= 1
        j -= 1
    else:
        if LCS[i - 1][j] > LCS[i][j - 1]:
            i -= 1
        else:
            j -= 1


