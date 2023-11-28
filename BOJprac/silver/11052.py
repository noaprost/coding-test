# 카드 구매하기

import sys

n = int(sys.stdin.readline())
cards = [0] + list(map(int, sys.stdin.readline().split()))

table = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            table[i][j] = cards[i]
        elif i > j:
            continue
        elif j % i == 0:
            table[i][j] = cards[i] * (j // i)
        elif j % i != 0:
            table[i][j] = cards[i] * (j // i) + cards[j % i]

for t in table:
    print(t)

ans = []
for t in table:
    ans.append(t[-1])

print(max(ans))
