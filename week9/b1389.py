# 케빈 베이컨의 6단계 법칙
# BFS 먼저
# 안되면 플로이드 워셜 알고리즘 이용

import sys
from queue import PriorityQueue

# 0 []
# 1 [3, 4]
# 2 []
# 3 [2]
# 4 [5, 3]
# 5 []

node, edge = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(node + 1)]
dis = [0 for _ in range(node + 1)]

que = PriorityQueue()

# 노드 사이에 간선 추가
i = 0
while i < edge:
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    i = i + 1

# 탐색 시작
