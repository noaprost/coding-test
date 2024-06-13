# 18436
# 14428
import sys

sys.setrecursionlimit(10**5)


def init(node, left, right):
    if left == right:
        if nums[left] % 2 == 0:
            seg[node] = (1, 0)  # 짝, 홀
        else:
            seg[node] = (0, 1)
        return seg[node]

    mid = (left + right) // 2
    l = init(node * 2, left, mid)
    r = init(node * 2 + 1, mid + 1, right)
    seg[node] = (l[0] + r[0], l[1] + r[1])
    return seg[node]


def query(node, left, right, start, end):
    if start <= left and end >= right:
        return seg[node]

    elif start > right or end < left:
        return (0, 0)

    else:
        mid = (left + right) // 2
        l = query(node * 2, left, mid, start, end)
        r = query(node * 2 + 1, mid + 1, right, start, end)
        return (l[0] + r[0], l[1] + r[1])


def update(node, left, right, idx, value):
    if idx < left or idx > right:
        return (0, 0)

    if left == idx and right == idx:
        if value % 2 == 0:
            seg[node] = (1, 0)
        else:
            seg[node] = (0, 1)
        return seg[node]

    mid = (left + right) // 2

    if mid >= idx:
        l = seg[node * 2 + 1]
        r = update(node * 2, left, mid, idx, value)
        seg[node] = (l[0] + r[0], l[1] + r[1])
    else:
        l = seg[node * 2]
        r = update(node * 2 + 1, mid + 1, right, idx, value)
        seg[node] = (l[0] + r[0], l[1] + r[1])

    return seg[node]


n = int(sys.stdin.readline())
nums = [0] + list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

seg = [0] * (4 * n)
init(1, 1, n)

for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    if c == 1:
        update(1, 1, n, a, b)
    elif c == 2:
        if a > b:
            print(query(1, 1, n, b, a)[0])
        else:
            print(query(1, 1, n, a, b)[0])
    else:
        if a > b:
            print(query(1, 1, n, b, a)[1])
        else:
            print(query(1, 1, n, a, b)[1])
