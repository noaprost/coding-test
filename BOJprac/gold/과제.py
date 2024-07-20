# 13904
import sys

n = int(sys.stdin.readline())
work = []
visited = [False for _ in range(1001)]
ans = 0

for _ in range(n):
    d, w = map(int, sys.stdin.readline().split())
    work.append((w, d))

work.sort(reverse=True)

for w, d in work:
    while d > 0 and visited[d] == True:
        d -= 1

    if d == 0:
        continue

    visited[d] = True
    ans += w

print(ans)
