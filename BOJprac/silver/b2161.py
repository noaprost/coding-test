# 카드1
from queue import Queue

n = int(input())
que = Queue()

if n == 1:  # 카드가 1장이면
    print(1)
else:
    for i in range(1, n + 1):  # 큐에 짝수만 담음
        que.put(i)

    while que.qsize() != 1:
        print(que.get(), end=" ")  # 버리기 먼저
        que.put(que.get())

    print(que.get())
