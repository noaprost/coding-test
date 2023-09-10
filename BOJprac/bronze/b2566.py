import sys

# 최대값 배열에서 가장큰 애의 위치가 행
# 그 줄에서 어디에 index가 있는지 확인하면 열
ai, aj = 0, 0
a = []
m = []
for i in range(9):
    tmp = list(map(int, sys.stdin.readline().split()))
    a.append(tmp)
    m.append(max(tmp))

ai = m.index(max(m))

for j in range(9):
    if a[ai][j] == max(m):
        aj = j
        break

print(max(m))
print(ai + 1, aj + 1)
