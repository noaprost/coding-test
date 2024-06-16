# 16975
import sys


def init(node, start, end):
    if start == end:
        seg[node] = nums[start]
        return

    mid = (start + end) // 2
    init(node * 2, start, mid)
    init(node * 2 + 1, mid + 1, end)
    seg[node] = seg[node * 2] + seg[node * 2 + 1]
    return


def update(node, start, end, left, right, diff):
    mid = (start + end) // 2
    if left <= start and right >= end:
        lazy[node] += (end - start + 1) * diff
    seg[node] += lazy[node]

    if start != end and lazy[node] != 0:
        lazy[2 * node] += (lazy[node] // (end - start + 1)) * (mid - start + 1)
        lazy[2 * node + 1] += (lazy[node] // (end - start + 1)) * (end - mid)
    lazy[node] = 0

    if (left <= start and right >= end) or right < start or end < left:
        return

    update(2 * node, start, mid, left, right, diff)
    update(2 * node + 1, mid + 1, end, left, right, diff)
    seg[node] = seg[node * 2] + seg[node * 2 + 1]
    return


def query(node, start, end, left, right):
    mid = (start + end) // 2
    seg[node] += lazy[node]
    if start != end and lazy[node] != 0:
        lazy[2 * node] += (lazy[node] // (end - start + 1)) * (mid - start + 1)
        lazy[2 * node + 1] += (lazy[node] // (end - start + 1)) * (end - mid)
    lazy[node] = 0

    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return seg[node]

    return query(node * 2, start, mid, left, right) + query(
        node * 2 + 1, mid + 1, end, left, right
    )


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
seg = [0] * (4 * n)
lazy = [0] * (4 * n)
init(1, 0, n - 1)

m = int(sys.stdin.readline())
for _ in range(m):
    command, *q = map(int, sys.stdin.readline().split())
    if command == 1:
        a, b, diff = q
        update(1, 0, n - 1, a - 1, b - 1, diff)
    else:
        x = q[0]
        print(query(1, 0, n - 1, x - 1, x - 1))
