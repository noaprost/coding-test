# 프린터 큐

import sys
from queue import Queue

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    que = Queue()

    docNum, docLoc = map(int, sys.stdin.readline().split())

    importance = list(map(int, sys.stdin.readline().split()))

    for i in range(len(importance)):
        que.put([i, importance[i]])

    m = max(importance)
    count = 0

    while que.qsize() != 0:
        v = que.get()

        if v[1] < m:
            que.put(v)
        else:
            count += 1
            if v[0] == docLoc:
                print(count)
                break
            else:
                importance.remove(v[1])
                m = max(importance)
