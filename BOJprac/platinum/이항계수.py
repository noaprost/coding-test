# 3651
import sys


def nCr(n, r):
    ret = 1

    for i in range(r):
        ret *= n - i

    for i in range(r):
        ret //= r - i

    return ret


n = int(sys.stdin.readline())
ans = []

for r in range(1, 31):
    low, high = r * 2, n + 1

    while low + 1 < high:
        mid = (low + high) // 2

        if nCr(mid, r) <= n:
            low = mid
        else:
            high = mid

    if nCr(low, r) == n:
        ans.append((low, r))

        if r < low - r:
            ans.append((low, low - r))

ans.sort()

print(len(ans))
for [a, b] in ans:
    print("{0} {1}".format(a, b))
