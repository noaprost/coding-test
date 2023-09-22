import sys

n, m = map(int, sys.stdin.readline().split())

card = list(map(int, sys.stdin.readline().split()))

blackJack = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if card[i] != card[j] and card[j] != card[k] and card[i] != card[k]:
                if card[i] + card[j] + card[k] <= m:
                    tmp = card[i] + card[j] + card[k]
                    if tmp > blackJack:
                        blackJack = tmp

print(blackJack)
