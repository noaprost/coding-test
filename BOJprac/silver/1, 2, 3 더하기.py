# 1을 만드는 경우의 수 -> 1
# 2을 만드는 경우의 수 -> 2
# 3을 만드는 경우의 수 -> 4
import sys

caseNum = int(sys.stdin.readline())
for _ in range(caseNum):
    n = int(sys.stdin.readline())
    ans = [1, 2, 4]
    for i in range(3, n):
        ans.append(ans[i - 1] + ans[i - 2] + ans[i - 3])

    print(ans[n - 1])
