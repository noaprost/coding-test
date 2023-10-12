import sys
from queue import Queue

w, h = -1, -1


def isIsland(maps):
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j] == 1:
                return i, j
    return -1, -1


while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0:
        break

    maps = []
    # map 입력(휴.. 힘들었다)
    if w == 1 and h == 1:
        maps.append(int(sys.stdin.readline()))
    elif h == 1:
        maps.append(list(map(int, sys.stdin.readline().split())))
    else:
        for i in range(h):
            maps.append(list(map(int, sys.stdin.readline().split())))

    # 섬의 개수 세기
    que = Queue()
    count = 0
    if h == 1:
        visited = [[False for _ in range(w)]]
    else:
        visited = [[False for _ in range(w)] for _ in range(h)]

    if w == 1 and h == 1:
        if maps[0] == 1:
            count += 1
        else:
            count = 0
    else:
        x, y = isIsland(maps)

        while x != -1:
            que.put([x, y])

            while que.qsize() != 0:
                v = que.get()
                x = v[0]
                y = v[1]
                visited[x][y] = True

                if x > 0 and not visited[x - 1][y] and maps[x - 1][y] == 1:
                    que.put([x - 1, y])
                    visited[x - 1][y] = True

                if x < h - 1 and not visited[x + 1][y] and maps[x + 1][y] == 1:
                    que.put([x + 1, y])
                    visited[x + 1][y] = True

                if y > 0 and not visited[x][y - 1] and maps[x][y - 1] == 1:
                    que.put([x, y - 1])
                    visited[x][y - 1] = True

                if y < w - 1 and not visited[x][y + 1] and maps[x][y + 1] == 1:
                    que.put([x, y + 1])
                    visited[x][y + 1] = True

                if (
                    x > 0
                    and y > 0
                    and not visited[x - 1][y - 1]
                    and maps[x - 1][y - 1] == 1
                ):
                    que.put([x - 1, y - 1])
                    visited[x - 1][y - 1] = True

                if (
                    x < h - 1
                    and y > 0
                    and not visited[x + 1][y - 1]
                    and maps[x + 1][y - 1] == 1
                ):
                    que.put([x + 1, y - 1])
                    visited[x + 1][y - 1] = True

                if (
                    x > 0
                    and y < w - 1
                    and not visited[x - 1][y + 1]
                    and maps[x - 1][y + 1] == 1
                ):
                    que.put([x - 1, y + 1])
                    visited[x - 1][y + 1] = True

                if (
                    x < h - 1
                    and y < w - 1
                    and not visited[x + 1][y + 1]
                    and maps[x + 1][y + 1] == 1
                ):
                    que.put([x + 1, y + 1])
                    visited[x + 1][y + 1] = True

            count += 1
            x, y = isIsland(maps)
    print(count)
