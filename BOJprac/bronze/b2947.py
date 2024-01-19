# 나무조각
import sys

tree = list(map(int, sys.stdin.readline().split()))
length = len(tree)

for i in range(length):
    for j in range(length - 1):
        if tree[j] > tree[j + 1]:
            tree[j], tree[j + 1] = tree[j + 1], tree[j]
            print(*tree)
