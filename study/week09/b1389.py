# 케빈 베이컨의 6단계 법칙
# BFS만으로는 안됨
# 다익스트라 여러번 or 플로이드 워셜 알고리즘 한번 이용

import sys

# 0 []
# 1 [3, 4]
# 2 []
# 3 [2]
# 4 [5, 3]
# 5 []

node, edge = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(node)]

# 노드 사이에 간선 추가
i = 0
while i < edge:
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    i = i + 1

# 탐색 시작
