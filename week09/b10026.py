# 적록색약
# BFS, 큐 이용
# 위아래양옆 검사해서 알파벳 같은거면 큐에 위치 넣고 넣은 곳은 방문 표시 후
# 반복하다가 더이상 갈곳이 없으면 구역에 +1하고
# 아직 방문하지 않은 다음 정점부터 다시 시작
# 모든 정점을 방문할 때까지

import sys
from queue import Queue
import copy


def findZero():
    for x in range(n):
        if 0 in visited[x]:
            y = visited[x].index(0)
            return x, y
    return -1, -1


def rgbSearch(map, count):
    x, y = 0, 0
    while x != -1:
        color = map[x][y]
        visited[x][y] = 1
        que.put([x, y])
        while que.qsize() != 0:
            tmp = que.get()
            x = tmp[0]
            y = tmp[1]
            if x > 0:
                if visited[x - 1][y] != 1 and color == map[x - 1][y]:
                    que.put([x - 1, y])
                    visited[x - 1][y] = 1

            if x < n - 1:
                if visited[x + 1][y] != 1 and color == map[x + 1][y]:
                    que.put([x + 1, y])
                    visited[x + 1][y] = 1

            if y > 0:
                if visited[x][y - 1] != 1 and color == map[x][y - 1]:
                    que.put([x, y - 1])
                    visited[x][y - 1] = 1

            if y < n - 1:
                if visited[x][y + 1] != 1 and color == map[x][y + 1]:
                    que.put([x, y + 1])
                    visited[x][y + 1] = 1

        x, y = findZero()
        count = count + 1
    return count


que = Queue()

n = int(sys.stdin.readline())

visited = [[0 for _ in range(n)] for _ in range(n)]

rgbCount, rgCount = 0, 0

# map 입력
rgbMap = [list(sys.stdin.readline().strip()) for _ in range(n)]
rgMap = copy.deepcopy(rgbMap)  # 깊은 복사

# 적록색약 map은 R = G로 바꿔줌
for i in range(n):
    for j in range(n):
        if rgMap[i][j] == "G":
            rgMap[i][j] = "R"


# 일반 사람
rgbCount = rgbSearch(rgbMap, rgbCount)

# 방문 기록 초기화
visited = [[0 for _ in range(n)] for _ in range(n)]

# 적록색약
rgCount = rgbSearch(rgMap, rgCount)

print(rgbCount, rgCount)
