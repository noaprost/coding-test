# 14890
import sys

n, L = map(int, sys.stdin.readline().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

# 가로길 검사
for i in range(n - 1):
    Lcount = 1
    for j in range(n - 1):
        if maps[i][j] == maps[i][j + 1]:
            Lcount += 1
        # 현재 높이가 다음 길의 높이보다 높다면 1.높이 검사 2.뒤로 L만큼의 평지가 유지되는가 -> for문으로 검사하지 않고 flag를 세워야되나
        if maps[i][j] > maps[i][j + 1]:
            if maps[i][j] - maps[i][j + 1] != 1:
                break

            for k in range(1, L + 1):
                if maps[i][j + 1] != maps[i][j + k]:
                    break
            j += 2
            Lcount = 0
        # 현재 높이가 다음 길의 높이보다 낮다면 1.높이 검사 2.지나온 길의 평지가 L만큼 유지되었는가 -> 이건 현재 평지가 몇만큼 이어졌는지 카운트를 해줌

# 세로길 검사
# for i in range(n):
#     for j in range(n):
