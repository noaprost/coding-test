# 14427
import sys

sys.setrecursionlimit(10**5)


def init(node, left, right):
    if left == right:
        seg[node] = (nums[left], left)
        return seg[node]

    mid = (left + right) // 2
    seg[node] = min(init(node * 2, left, mid), init(node * 2 + 1, mid + 1, right))
    return seg[node]


def query(node, left, right, start, end):
    if start <= left and end >= right:
        return seg[node]

    elif start > right or end < left:
        return (1000000001, 100001)

    else:
        mid = (left + right) // 2
        return min(
            query(node * 2, left, mid, start, end),
            query(node * 2 + 1, mid + 1, right, start, end),
        )


def update(node, left, right, idx, value):
    if idx < left or idx > right:
        return (1000000001, 100001)

    if left == idx and right == idx:
        seg[node] = (value, idx)
        return seg[node]

    mid = (left + right) // 2

    if mid >= idx:
        seg[node] = min(seg[node * 2 + 1], update(node * 2, left, mid, idx, value))
    else:
        seg[node] = min(seg[node * 2], update(node * 2 + 1, mid + 1, right, idx, value))

    return seg[node]


n = int(sys.stdin.readline())
nums = [0] + list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

seg = [0] * (4 * n)
init(1, 1, n)

for _ in range(m):
    c = sys.stdin.readline().rstrip()
    if c[0] == "1":
        _, a, b = map(int, c.split())
        update(1, 1, n, a, b)
    elif c[0] == "2":
        print(query(1, 1, n, 1, n)[1])
