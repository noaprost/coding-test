# 7453
import sys

n = int(sys.stdin.readline())

a_list, b_list, c_list, d_list = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    d_list.append(d)

AandB = []
for a in a_list:
    for b in b_list:
        AandB.append(a + b)
AandB.sort()

CandD = []
for c in c_list:
    for d in d_list:
        CandD.append(c + d)
CandD.sort()

ans = 0
left, right = 0, len(CandD) - 1
sum = 0

while 0 <= right and left < len(AandB):
    sum = AandB[left] + CandD[right]
    if sum < 0:
        left += 1
    elif sum > 0:
        right -= 1
    else:
        x = 1
        for i in range(left + 1, len(AandB)):
            if AandB[left] == AandB[i]:
                x += 1
            else:
                break
        y = 1
        for i in range(right - 1, -1, -1):
            if CandD[right] == CandD[i]:
                y += 1
            else:
                break
        ans += x * y
        left += x
        right -= y

print(ans)
