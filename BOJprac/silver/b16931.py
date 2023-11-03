# 겉넓이 구하기

import sys

n, m = map(int, sys.stdin.readline().split())

shape = []

area = 0

for _ in range(n):
    if m == 1:
        shape.append([int(sys.stdin.readline())])
    else:
        shape.append(list(map(int, sys.stdin.readline().split())))

# 윗 + 밑면
area += n * m * 2

# 왼면 v
for i in range(m):
    for j in range(n):
        if j == n - 1:
            area += shape[j][i]
            break
        else:
            if shape[j][i] >= shape[j + 1][i]:
                area += shape[j][i] - shape[j + 1][i]

# 오른면 v
for i in range(m):
    for j in range(n - 1, -1, -1):
        if j == 0:
            area += shape[j][i]
            break
        else:
            if shape[j][i] >= shape[j - 1][i]:
                area += shape[j][i] - shape[j - 1][i]

# 앞면
for i in range(n):
    for j in range(m - 1, -1, -1):
        if j == 0:
            area += shape[i][j]
            break
        else:
            if shape[i][j] >= shape[i][j - 1]:
                area += shape[i][j] - shape[i][j - 1]

# 뒷면
for i in range(n):
    for j in range(m):
        if j == m - 1:
            area += shape[i][j]
            break
        else:
            if shape[i][j] >= shape[i][j + 1]:
                area += shape[i][j] - shape[i][j + 1]

print(area)
