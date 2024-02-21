# 9205
import sys
from queue import Queue

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    isHappy = False
    conNum = int(sys.stdin.readline())
    loc = []
    start = list(map(int, sys.stdin.readline().split()))
    for i in range(1, conNum + 1):
        tmp = list(map(int, sys.stdin.readline().split()))
        tmp.append(i)
        loc.append(tmp)
    end = list(map(int, sys.stdin.readline().split()))
    loc.append([end[0], end[1], conNum + 1])
    visited = [True] + [False for _ in range(conNum + 1)]
    que = Queue()
    que.put([start[0], start[1], 0])
    while que.qsize() != 0:
        v = que.get()
        visited[v[2]] = True

        if v[0] == end[0] and v[1] == end[1]:
            print("happy")
            isHappy = True
            break

        for lo in loc:
            if not visited[lo[2]] and abs(v[0] - lo[0]) + abs(v[1] - lo[1]) <= 1000:
                visited[lo[2]] = True
                que.put(lo)
    if not isHappy:
        print("sad")
