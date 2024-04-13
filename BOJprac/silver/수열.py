import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))


dp1 = []
dp2 = []
for i in range(n):
    if i == 0:
        dp1.append(i + 1)
    else:
        if arr[i] >= arr[i - 1]:
            dp1.append(dp1[i - 1] + 1)
        else:
            dp1.append(1)

for i in range(n):
    if i == 0:
        dp2.append(i + 1)
    else:
        if arr[i] <= arr[i - 1]:
            dp2.append(dp2[i - 1] + 1)
        else:
            dp2.append(1)
print(max(max(dp1), max(dp2)))
