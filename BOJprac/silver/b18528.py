# 큐에 대한 기본 지식이라며어.. 왜 덱으로 풀어야 풀리게 만들어 놓은건뎅... 힝구

import sys
from collections import deque

que = deque()

commandNum = int(sys.stdin.readline())

for _ in range(commandNum):
    com = sys.stdin.readline().rstrip()
    if com[:2] == "pu":
        c, v = com.split()
        que.append(int(v))

    elif com == "pop":
        if not que:
            print(-1)
        else:
            t = que.popleft()
            print(t)

    elif com == "size":
        print(len(que))

    elif com == "empty":
        if not que:
            print(1)
        else:
            print(0)

    elif com == "front":
        if not que:
            print(-1)
        else:
            print(que[0])

    elif com == "back":
        if not que:
            print(-1)
        else:
            print(que[-1])
