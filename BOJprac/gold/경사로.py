# 14890
import sys

n, L = map(int, sys.stdin.readline().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

ans = 0

# 가로길 검사
for i in range(n):
    j = 1
    curHeight = maps[i][0]
    flag = 1
    visited = [False] * n
    while j < n:
        if abs(curHeight - maps[i][j]) > 1:
            flag = 0
            break
        else:
            if curHeight == maps[i][j]:
                j += 1

            elif curHeight < maps[i][j]:
                tmpHeight = maps[i][j - 1]

                for k in range(0, L):
                    if j - k - 1 >= 0:
                        if not visited[j - k - 1]:
                            if tmpHeight != maps[i][j - k - 1]:
                                flag = 0
                            else:
                                visited[j - k - 1] = True
                        else:
                            flag = 0
                    else:
                        flag = 0

                if not flag:
                    break
                else:
                    curHeight = maps[i][j]
                    j += 1

            elif curHeight > maps[i][j]:
                tmpHeight = maps[i][j]

                for k in range(0, L):
                    if j + k < n:
                        if not visited[j + k]:
                            if tmpHeight != maps[i][j + k]:
                                flag = 0
                            else:
                                visited[j + k] = True
                        else:
                            flag = 0
                    else:
                        flag = 0

                if not flag:
                    break
                else:
                    curHeight = maps[i][j]
                    j += L
    if flag:
        ans += 1

# 세로길 검사
for i in range(n):
    j = 1
    curHeight = maps[0][i]
    flag = 1
    visited = [False] * n
    while j < n:
        if abs(curHeight - maps[j][i]) > 1:
            flag = 0
            break
        else:
            if curHeight == maps[j][i]:
                j += 1

            elif curHeight < maps[j][i]:
                tmpHeight = maps[j - 1][i]

                for k in range(0, L):
                    if j - k - 1 >= 0:
                        if not visited[j - k - 1]:
                            if tmpHeight != maps[j - k - 1][i]:
                                flag = 0
                            else:
                                visited[j - k - 1] = True
                        else:
                            flag = 0
                    else:
                        flag = 0

                if not flag:
                    break
                else:
                    curHeight = maps[j][i]
                    j += 1

            elif curHeight > maps[j][i]:
                tmpHeight = maps[j][i]

                for k in range(0, L):
                    if j + k < n:
                        if not visited[j + k]:
                            if tmpHeight != maps[j + k][i]:
                                flag = 0
                            else:
                                visited[j + k] = True
                        else:
                            flag = 0
                    else:
                        flag = 0

                if not flag:
                    break
                else:
                    curHeight = maps[j][i]
                    j += L
    if flag:
        ans += 1

print(ans)
