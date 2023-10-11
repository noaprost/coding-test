# 치즈
# 핵심 idea : 치즈 한 칸의 tbrl중 하나라도 공기면과 닿아있다면 그 치즈는 녹을 예정

# 1번 시도 -> bfs를 돌려서 치즈판이 전부 비워질때까지 반복하면서
# 겉면의 치즈를 찾아서 배열에 저장하고 비워주고
# 그러다가 전부 비워지면 마지먹에 저장되었던 배열의 길이가 곧 마지막까지 남은 치즈의 개수
# 날짜 계산은 치즈 배열 하나 완성, 비우기 과정때마다 +1 씩 해줌

# <출력>
# 시간
# 남은 치즈 조각 개수

import sys
from queue import Queue

# 이것저것 선언하고 입력
n, m = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
que = Queue()
fade = []
hours = 0


def isVisit(visited):
    for v in visited:
        if False in v:
            return False
    return True


# 초기 상태
x, y = 0, 0
que.put([x, y])
lastLen = 0

while True:
    fade = []

    while que.qsize() != 0:
        v = que.get()
        x = v[0]
        y = v[1]
        visited[x][y] = True

        if x > 0 and not visited[x - 1][y]:
            if cheese[x - 1][y] == 1:
                fade.append([x - 1, y])
                visited[x - 1][y] = True
            else:
                que.put([x - 1, y])
                visited[x - 1][y] = True

        if x < n - 1 and not visited[x + 1][y]:
            if cheese[x + 1][y] == 1:
                fade.append([x + 1, y])
                visited[x + 1][y] = True
            else:
                que.put([x + 1, y])
                visited[x + 1][y] = True

        if y > 0 and not visited[x][y - 1]:
            if cheese[x][y - 1] == 1:
                fade.append([x, y - 1])
                visited[x][y - 1] = True
            else:
                que.put([x, y - 1])
                visited[x][y - 1] = True

        if y < m - 1 and not visited[x][y + 1]:
            if cheese[x][y + 1] == 1:
                fade.append([x, y + 1])
                visited[x][y + 1] = True
            else:
                que.put([x, y + 1])
                visited[x][y + 1] = True

    if len(fade) != 0:
        lastLen = len(fade)
        for f in fade:
            que.put(f)
        hours += 1

    if isVisit(visited):
        print(hours)
        print(lastLen)
        exit()
