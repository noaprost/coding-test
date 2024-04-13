import sys
from queue import Queue

caseNum = int(sys.stdin.readline())


# 다음 배추의 위치를 찾아줌
def findFalse(m):
    for x in range(m):
        if False in visited[x]:
            y = visited[x].index(False)
            return x, y
    return -1, -1


for _ in range(caseNum):
    # 필드 생성
    m, n, k = map(int, sys.stdin.readline().split())

    total = 0

    # nxm 크기의 배추밭
    field = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[True for _ in range(n)] for _ in range(m)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[x][y] = 1  # 배추가 심어진 부분 표시
        visited[x][y] = False

    # 필드 생성 끝

    que = Queue()
    x, y = findFalse(m)

    while x != -1:
        visited[x][y] = True
        que.put([x, y])

        while que.qsize() != 0:
            tmp = que.get()
            x = tmp[0]
            y = tmp[1]

            if x > 0:
                if not visited[x - 1][y] and field[x - 1][y] == 1:
                    que.put([x - 1, y])
                    visited[x - 1][y] = True
            if x < m - 1:
                if not visited[x + 1][y] and field[x + 1][y] == 1:
                    que.put([x + 1, y])
                    visited[x + 1][y] = True
            if y > 0:
                if not visited[x][y - 1] and field[x][y - 1] == 1:
                    que.put([x, y - 1])
                    visited[x][y - 1] = True
            if y < n - 1:
                if not visited[x][y + 1] and field[x][y + 1] == 1:
                    que.put([x, y + 1])
                    visited[x][y + 1] = True

        x, y = findFalse(m)
        total += 1

    print(total)
