# 카드2
# 큐 이용
from queue import Queue

n = int(input())
que = Queue()

if n == 1:  # 카드가 1장이면 
    print(1)
else:
    for i in range(2, n + 1, 2):  # 큐에 짝수만 담음
        que.put(i)

    if n % 2 == 0:  # 카드 개수가 짝수였으면
        while que.qsize() != 1:
            que.get()  # 버리기 먼저
            que.put(que.get())
    else:  # 카드 개수가 홀수였으면
        while que.qsize() != 1:
            que.put(que.get())  # 뒤로 보내기 먼저
            que.get()

    print(que.get())


# 규칙 이용
# 4 -> 4
# 6 -> 4
# 8 -> 8
# 10 -> 4
# 12 -> 8
# 14 -> 12
# 16 -> 16
# 18 -> 4
# 20 -> 8

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
