# 1715
import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
que = PriorityQueue()
for _ in range(n):
    v = int(sys.stdin.readline())
    que.put(v)

ans = 0

while que.qsize() != 1:
    v1 = que.get()
    v2 = que.get()
    ans += v1 + v2
    que.put(v1 + v2)

print(ans)
