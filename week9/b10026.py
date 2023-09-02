# 적록색약
# BFS, 큐 이용
# 위아래양옆 검사해서 알파벳 같은거면 큐에 위치 넣고 넣은 곳은 방문 표시 후
# 반복하다가 더이상 갈곳이 없으면 구역에 +1하고
# 아직 방문하지 않은 다음 정점부터 다시 시작
# 모든 정점을 방문할 때까지

import sys
from queue import Queue


que = Queue()

n = int(sys.stdin.readline())

# 적록색약 map 입력
rgbMap = [list(sys.stdin.readline().strip()) for _ in range(n)]

print(rgbMap)
