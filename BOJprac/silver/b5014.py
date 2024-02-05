# 스타트링크
# 주어진 조건에 맞게 층을 방문하다가 도착하지도 못했는데 모든 층에 방문했다면 갈 수 없음 표시
# 중간에 도착하면 바로 출력
import sys
from queue import Queue

totalFloor, start, end, up, down = map(int, sys.stdin.readline().split())
if start == end:
    exit(print(0))

count = 0
building = [i for i in range(totalFloor + 1)]
visited = [True] + [False for _ in range(totalFloor)]
que = Queue()
que.put(start)
visited[start] = True
while que.qsize() != 0:
    v = que.get()

    if v == end:
        exit(print(count))

    if v < end:
        if up == 0:
            exit(print("use the stairs"))
        if v + up <= totalFloor:
            if not visited[v + up]:
                que.put(v + up)
                visited[v + up] = True
                count += 1
        elif v - down >= 1:
            if not visited[v - down]:
                que.put(v - down)
                visited[v - down] = True
                count += 1
        else:
            exit(print("use the stairs"))

    if v > end:
        if down == 0:
            exit(print("use the stairs"))
        if v - down >= 1:
            if not visited[v - down]:
                que.put(v - down)
                visited[v - down] = True
                count += 1
        elif v + up <= totalFloor:
            if not visited[v + up]:
                que.put(v + up)
                visited[v + up] = True
                count += 1
        else:
            exit(print("use the stairs"))

print("use the stairs")
