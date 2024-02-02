# 트리 순회
import sys

n = int(sys.stdin.readline())
graph = []
nodes = []
for i in range(n):
    graph.append(list(sys.stdin.readline().split()))
    nodes.append(graph[i][0])

visited = [False for _ in range(n)]


def preorder(node):
    if node != ".":
        idx = nodes.index(node)
        # 노드 순회
        print(node, end="")
        # 왼쪽 순회
        preorder(graph[idx][1])
        # 오른쪽 순회
        preorder(graph[idx][2])


def postorder(node):
    if node != ".":
        idx = nodes.index(node)
        # 왼쪽 순회
        postorder(graph[idx][1])
        # 노드 순회
        print(node, end="")
        # 오른쪽 순회
        postorder(graph[idx][2])


def levelorder(node):
    if node != ".":
        idx = nodes.index(node)
        # 왼쪽 순회
        levelorder(graph[idx][1])
        # 오른쪽 순회
        levelorder(graph[idx][2])
        # 노드 순회
        print(node, end="")


preorder("A")
print()
postorder("A")
print()
levelorder("A")
