# 카드 합체 놀이
import sys
from queue import PriorityQueue

n, count = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

que = PriorityQueue()

for card in cards:
    que.put(card)

for _ in range(count):
    a = que.get()
    b = que.get()

    que.put(a + b)
    que.put(a + b)

sum = 0
while que.qsize() != 0:
    s = que.get()
    sum += s

print(sum)
