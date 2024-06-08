# 2357
import sys

sys.setrecursionlimit(10**5)


def init(node, left, right):
    if left == right:
        seg[node] = nums[left]
        return seg[node]

    mid = (left + right) // 2
    seg[node] = min(init(node * 2, left, mid), init(node * 2 + 1, mid + 1, right))
    return seg[node]


def query(node, left, right, start, end):
    if start <= left and end >= right:
        return seg[node]

    elif start > right or end < left:
        return 1000000000

    else:
        mid = (left + right) // 2
        return min(
            query(node * 2, left, mid, start, end),
            query(node * 2 + 1, mid + 1, right, start, end),
        )


n, m = map(int, sys.stdin.readline().split())
nums = [-1]

for _ in range(n):
    a = int(sys.stdin.readline())
    nums.append(a)

seg = [0] * (4 * n)
init(1, 1, n)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(query(1, 1, n, a, b))
