# 카드2
# 큐 이용
from queue import Queue

n = int(input())
que = Queue()

if n == 1:
    print(1)
else:
    for i in range(2, n + 1, 2):
        que.put(i)

    if n % 2 == 0:
        while que.qsize() != 1:
            que.get()
            que.put(que.get())
    else:
        while que.qsize() != 1:
            que.put(que.get())
            que.get()

    print(que.get())

# 규칙 이용
n = int(input())
p = 1
if n == 1:
    print(1)
else:
    while n > 2**p:
        p += 1
    p -= 1
    tmp = n - (2**p)
    answer = 2 * tmp
    print(int(answer))
