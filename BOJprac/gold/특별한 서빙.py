# 27896
import sys
from queue import PriorityQueue

n, angry = map(int, sys.stdin.readline().split())

student = list(map(int, sys.stdin.readline().split()))

que = PriorityQueue()

sum = 0
gaji = 0

for i in range(n):
    sum += student[i]
    que.put(-student[i])
    if sum >= angry:
        tmp = que.get()
        sum += tmp * 2
        gaji += 1

print(gaji)
