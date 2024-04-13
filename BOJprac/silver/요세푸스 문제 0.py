import sys

n, k = map(int, sys.stdin.readline().split())

que = [i for i in range(1, n + 1)]

front = 0

print("<", end="")
while len(que) != 1:
    front += k - 1
    front = front % len(que)
    print(que[front], end=", ")
    que.remove(que[front])

print(que[0], end="")
print(">")
