# 쉬운 최단거리
# 목표가 어디에 있는지 내가 어떻게 알고 한 방향을 선택해서 이동하지..
# 그래도 일단은 최단거리니까 bfs로 가야겠지..?
# TBLR 순


# 1. 담으려는게 0인 경우 -> 안담음 / 경로 개수 그대로
# 2. 담으려는게 1인 경우 -> 큐에 담음 / 경로 개수 +1
# 3. 담으려는게 2인 경우 -> 종료 / 경로 개수 출력

import sys
from queue import Queue

n, m = map(int, sys.stdin.readline().split())

# n x m map
map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

que = Queue()
