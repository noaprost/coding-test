# 2668
import sys


def dfs(v, s):
    visited[v] = True
    w = base[v]
    if not visited[w]:
        dfs(w, s)
    elif visited[w] and w == s:
        ans.append(w)


n = int(sys.stdin.readline())
base = [0] + [int(sys.stdin.readline()) for _ in range(n)]
ans = []

for i in range(1, n + 1):
    visited = [True] + [False for _ in range(n)]
    dfs(i, i)

ans.sort()
print(len(ans))
for a in ans:
    print(a)
